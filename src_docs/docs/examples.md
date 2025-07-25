---
title: Examples
description: Real-world examples and use cases for the MkDocs Output as Input plugin
---

# Examples

This page demonstrates various use cases and workflows for the MkDocs Output as Input plugin.

## Basic Examples

### Simple Documentation Site

Basic setup for extracting documentation content:

```yaml
# mkdocs.yml
site_name: My API Docs
plugins:
  - output-as-input:
      stage_dir: extracted
      html_element: main
```

Input (`docs/api.md`):
```markdown
---
title: API Reference
version: 1.0.0
category: reference
---

# API Reference

## GET /users

Returns a list of users.
```

Output (`extracted/api.md`):
```markdown
---
title: API Reference
version: 1.0.0
category: reference
---

<article>
<h1>API Reference</h1>
<h2>GET /users</h2>
<p>Returns a list of users.</p>
</article>
```

### Preserving Complex Frontmatter

The plugin preserves all YAML frontmatter:

```markdown
---
title: Advanced Page
date: 2024-01-20
authors:
  - name: Jane Doe
    email: jane@example.com
  - name: John Smith
tags: [tutorial, advanced, python]
metadata:
  difficulty: intermediate
  duration: 30min
  requirements:
    - Python 3.8+
    - MkDocs 1.4+
---

# Content here...
```

All frontmatter is preserved in the cousin file.

## Integration Examples

### Hugo Integration

Using the plugin to feed content into a Hugo site:

```yaml
# mkdocs.yml
plugins:
  - output-as-input:
      stage_dir: "../hugo-site/content/docs"
      html_element: "article"
      target_tag: "div"
```

```bash
# Build workflow
mkdocs build
cd ../hugo-site
hugo build
```

### Jekyll Blog Posts

Converting documentation to Jekyll blog posts:

```yaml
plugins:
  - output-as-input:
      stage_dir: "../jekyll/_posts"
      html_element: "main"
```

With custom frontmatter:
```markdown
---
title: "New Feature Release"
date: 2024-01-20
layout: post
categories: [releases, features]
---
```

### Docusaurus Integration

```yaml
plugins:
  - output-as-input:
      stage_dir: "../docusaurus/docs"
      html_element: ".md-content"
      target_tag: "div"
```

## Advanced Workflows

### Multi-Language Documentation

Process documentation for different languages:

```yaml
# mkdocs.yml
plugins:
  - output-as-input:
      stage_dir: "stage/${LANGUAGE}"
      html_element: "main"
      verbose: true
```

```bash
# Build for multiple languages
LANGUAGE=en mkdocs build
LANGUAGE=es mkdocs build -f mkdocs.es.yml
LANGUAGE=fr mkdocs build -f mkdocs.fr.yml
```

### API Documentation Pipeline

Extract API docs for further processing:

```python
# post_process.py
import os
import yaml
from pathlib import Path

stage_dir = Path("stage")
api_docs = []

for md_file in stage_dir.glob("api/*.md"):
    with open(md_file) as f:
        content = f.read()
        # Extract frontmatter
        if content.startswith("---"):
            _, fm, body = content.split("---", 2)
            metadata = yaml.safe_load(fm)
            api_docs.append({
                "endpoint": metadata.get("endpoint"),
                "method": metadata.get("method"),
                "content": body
            })

# Generate OpenAPI spec, Postman collection, etc.
```

### Print-Ready Documentation

Create print-optimized versions:

```yaml
plugins:
  - output-as-input:
      stage_dir: "print"
      html_element: "article"
      target_tag: "div"
```

```bash
# Convert to PDF
mkdocs build
pandoc print/*.md -o documentation.pdf \
  --template=mytemplate.tex \
  --pdf-engine=xelatex
```

### Search Index Generation

Build custom search indexes:

```python
# build_search.py
import json
from pathlib import Path
from bs4 import BeautifulSoup

search_index = []
stage_dir = Path("stage")

for md_file in stage_dir.glob("**/*.md"):
    with open(md_file) as f:
        content = f.read()
        # Parse HTML content
        if "<article>" in content:
            soup = BeautifulSoup(content, 'html.parser')
            article = soup.find('article')
            search_index.append({
                "path": str(md_file),
                "title": soup.find('h1').text if soup.find('h1') else "",
                "content": article.get_text(),
                "url": f"/{md_file.relative_to(stage_dir)}"
            })

with open("search_index.json", "w") as f:
    json.dump(search_index, f)
```

## Theme-Specific Examples

### Material for MkDocs

```yaml
theme:
  name: material

plugins:
  - output-as-input:
      html_element: "article.md-content__inner"
      stage_dir: "material-output"
```

### ReadTheDocs Theme

```yaml
theme:
  name: readthedocs

plugins:
  - output-as-input:
      html_element: "div.rst-content"
      stage_dir: "rtd-output"
```

### Custom Theme

```yaml
theme:
  name: custom
  custom_dir: overrides/

plugins:
  - output-as-input:
      html_element: "#custom-content"
      stage_dir: "custom-output"
```

## Debugging Examples

### Verbose Logging

Enable detailed logging to troubleshoot:

```yaml
plugins:
  - output-as-input:
      verbose: true
      stage_dir: "debug-output"
```

Output:
```
INFO: OutputAsInput: Processing page: index.md
DEBUG: OutputAsInput: Found frontmatter: {'title': 'Home', 'date': '2024-01-20'}
DEBUG: OutputAsInput: Extracted content from <main> element
INFO: OutputAsInput: Created cousin file: debug-output/index.md
```

### Testing Selectors

Test different HTML selectors:

```python
# test_selectors.py
from bs4 import BeautifulSoup

with open("site/index.html") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    
    selectors = ["main", "article", ".content", "#main-content"]
    for selector in selectors:
        element = soup.select_one(selector)
        if element:
            print(f"✓ Found {selector}: {len(element.text)} chars")
        else:
            print(f"✗ Not found: {selector}")
```