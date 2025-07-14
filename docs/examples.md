---
title: Examples
description: Real-world usage examples for the MkDocs Output as Input plugin
---

# Examples

This page provides practical examples of how to use the MkDocs Output as Input plugin in various scenarios.

## Basic Usage

### Simple Blog Post Processing

**Input** (`docs/posts/my-post.md`):
```markdown
---
title: My Blog Post
date: 2025-01-14
author: Jane Doe
tags: [python, documentation]
---

# My Blog Post

This is a **markdown** blog post with some content.
```

**Configuration** (`mkdocs.yml`):
```yaml
plugins:
  - output-as-input
```

**Output** (`stage/posts/my-post.md`):
```markdown
---
title: My Blog Post
date: 2025-01-14
author: Jane Doe
tags: [python, documentation]
---

<article class="md-content">
  <h1>My Blog Post</h1>
  <p>This is a <strong>markdown</strong> blog post with some content.</p>
</article>
```

## Multi-Stage Documentation Pipeline

### MkDocs → Hugo Pipeline

**Scenario**: Use MkDocs for authoring and Hugo for final site generation.

**MkDocs Configuration** (`mkdocs.yml`):
```yaml
site_name: My Documentation
theme:
  name: material

plugins:
  - search
  - output-as-input:
      stage_dir: hugo/content
      html_element: main
      target_tag: div
```

**Hugo Configuration** (`hugo.yaml`):
```yaml
contentDir: hugo/content
baseURL: https://example.com
```

**Build Script** (`build.sh`):
```bash
#!/bin/bash
set -e

echo "Building with MkDocs..."
mkdocs build

echo "Processing with Hugo..."
hugo --contentDir=hugo/content

echo "Done!"
```

### MkDocs → Jekyll Pipeline

**Configuration** (`mkdocs.yml`):
```yaml
plugins:
  - output-as-input:
      stage_dir: _posts
      html_element: article
      target_tag: div
```

**Post-processing** (`process.py`):
```python
import os
import re
from pathlib import Path

# Convert MkDocs output to Jekyll format
for md_file in Path("_posts").glob("**/*.md"):
    content = md_file.read_text()
    
    # Add Jekyll layout to frontmatter
    content = re.sub(
        r'(---\n.*?)\n---',
        r'\1\nlayout: post\n---',
        content,
        flags=re.DOTALL
    )
    
    md_file.write_text(content)
```

## Theme-Specific Examples

### Material Theme

**Extract inner content**:
```yaml
plugins:
  - output-as-input:
      html_element: article.md-content__inner
      target_tag: section
```

### ReadTheDocs Theme

**Extract main content**:
```yaml
plugins:
  - output-as-input:
      html_element: div.rst-content
      target_tag: article
```

### Custom Theme

**For a custom theme with specific structure**:
```yaml
plugins:
  - output-as-input:
      html_element: div.content-wrapper > div.main-content
      target_tag: main
```

## Content Processing Examples

### API Documentation

**Input** (`docs/api/users.md`):
```markdown
---
title: User API
api_version: v1
endpoint: /api/users
---

# User API

The User API allows you to manage users.

## GET /api/users

Returns a list of users.
```

**Configuration**:
```yaml
plugins:
  - mkdocstrings
  - output-as-input:
      stage_dir: api_docs
      html_element: main
      target_tag: section
```

### Tutorial Series

**Input** (`docs/tutorials/setup.md`):
```markdown
---
title: Setup Tutorial
series: getting-started
order: 1
difficulty: beginner
---

# Setup Tutorial

This tutorial will guide you through the setup process.
```

**Post-processing** to group by series:
```python
import yaml
from pathlib import Path
from collections import defaultdict

# Group tutorials by series
series_map = defaultdict(list)

for md_file in Path("stage/tutorials").glob("*.md"):
    with open(md_file) as f:
        content = f.read()
        
    # Extract frontmatter
    if content.startswith('---'):
        _, fm_text, body = content.split('---', 2)
        frontmatter = yaml.safe_load(fm_text)
        series = frontmatter.get('series', 'misc')
        
        series_map[series].append({
            'file': md_file,
            'title': frontmatter.get('title'),
            'order': frontmatter.get('order', 999)
        })

# Create index files for each series
for series, tutorials in series_map.items():
    tutorials.sort(key=lambda x: x['order'])
    
    index_content = f"# {series.title()} Series\n\n"
    for tutorial in tutorials:
        index_content += f"- [{tutorial['title']}]({tutorial['file'].name})\n"
    
    (Path("stage/tutorials") / f"{series}-index.md").write_text(index_content)
```

## Integration Examples

### GitHub Actions Workflow

**`.github/workflows/docs.yml`**:
```yaml
name: Documentation

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install mkdocs-material vexy-mkdocs-output-as-input
      
      - name: Build with MkDocs
        run: mkdocs build
      
      - name: Process staged files
        run: python scripts/process_stage.py
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
```

### Docker Multi-Stage Build

**`Dockerfile`**:
```dockerfile
# Stage 1: MkDocs build
FROM python:3.11-slim as mkdocs-builder
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY docs/ docs/
COPY mkdocs.yml .
RUN mkdocs build

# Stage 2: Hugo build
FROM hugomods/hugo:latest as hugo-builder
WORKDIR /app
COPY --from=mkdocs-builder /app/stage ./content
COPY hugo.yaml .
RUN hugo

# Stage 3: Final image
FROM nginx:alpine
COPY --from=hugo-builder /app/public /usr/share/nginx/html
```

## Debugging Examples

### Verbose Mode

**Enable detailed logging**:
```yaml
plugins:
  - output-as-input:
      verbose: true
```

**Sample output**:
```
INFO - OutputAsInput: site_dir=/app/site, docs_dir=/app/docs
INFO - OutputAsInput: Captured source index.md
INFO - OutputAsInput: Captured source getting-started.md
INFO - OutputAsInput: Creating stage directory at /app/stage
INFO - OutputAsInput: Created cousin file /app/stage/index.md
INFO - OutputAsInput: Created cousin file /app/stage/getting-started.md
INFO - OutputAsInput: Processed 2/2 files
```

### Testing Different Selectors

**Test script** (`test_selectors.py`):
```python
from bs4 import BeautifulSoup
from pathlib import Path

html_file = Path("site/index.html")
html_content = html_file.read_text()
soup = BeautifulSoup(html_content, 'html.parser')

selectors = [
    'main',
    'article',
    'div.content',
    'div.md-content',
    '#content',
    'main.md-content'
]

for selector in selectors:
    element = soup.select_one(selector)
    if element:
        print(f"✓ {selector}: Found element with {len(element.get_text())} characters")
    else:
        print(f"✗ {selector}: No element found")
```

## Best Practices

1. **Start simple**: Begin with default settings and adjust as needed
2. **Use verbose mode**: Enable verbose logging during development
3. **Test selectors**: Verify your HTML element selector works across pages
4. **Backup frontmatter**: The plugin preserves frontmatter, but always keep backups
5. **Version control**: Keep both source and stage directories under version control
6. **Document your pipeline**: Create clear documentation for your processing steps
