---
title: Troubleshooting Guide
description: Solutions to common issues with MkDocs Output as Input plugin
---

# Troubleshooting Guide

This guide helps you diagnose and fix common issues with the MkDocs Output as Input plugin.

## Diagnostic Checklist

Before diving into specific issues, run through this checklist:

1. **Enable verbose logging**:
   ```yaml
   plugins:
     - output-as-input:
         verbose: true
   ```

2. **Check MkDocs version**:
   ```bash
   mkdocs --version
   # Should be 1.4.0 or higher
   ```

3. **Verify plugin installation**:
   ```bash
   pip show vexy-mkdocs-output-as-input
   ```

4. **Test with minimal config**:
   ```yaml
   site_name: Test
   plugins:
     - output-as-input
   ```

## Common Issues

### Plugin Not Loading

**Symptoms:**
- No `stage/` directory created
- No plugin output in build logs
- Error: `Plugin 'output-as-input' not found`

**Solutions:**

1. **Reinstall the plugin**:
   ```bash
   pip uninstall vexy-mkdocs-output-as-input
   pip install vexy-mkdocs-output-as-input
   ```

2. **Check Python environment**:
   ```bash
   which python
   which mkdocs
   # Ensure both are in the same environment
   ```

3. **Verify plugin name**:
   ```yaml
   plugins:
     - output-as-input  # Correct
     # NOT: outputasinput, output_as_input, etc.
   ```

### No Output Files Created

**Symptoms:**
- Build succeeds but `stage/` directory is empty
- Verbose logs show no files processed

**Solutions:**

1. **Check source files exist**:
   ```bash
   ls docs/*.md
   ```

2. **Verify MkDocs processes files**:
   ```bash
   mkdocs build -v
   # Look for "Reading source files" messages
   ```

3. **Check nav configuration**:
   ```yaml
   # Files must be in nav or use_directory_urls
   nav:
     - Home: index.md
     - Guide: guide.md
   ```

### HTML Element Not Found

**Symptoms:**
- Warning: "No elements matching X found"
- Cousin files created but empty

**Solutions:**

1. **Inspect generated HTML**:
   ```bash
   # Check what MkDocs generated
   cat site/index.html | grep -E "<main|<article|class="
   ```

2. **Try different selectors**:
   ```yaml
   # For Material theme
   html_element: .md-content__inner
   
   # For ReadTheDocs
   html_element: .rst-content
   
   # Generic fallback
   html_element: body
   ```

3. **Use browser DevTools**:
   - Open generated site in browser
   - Inspect element structure
   - Copy selector from DevTools

### Frontmatter Issues

**Symptoms:**
- Frontmatter missing in output
- YAML parsing errors
- Malformed cousin files

**Solutions:**

1. **Validate YAML syntax**:
   ```yaml
   ---
   title: My Page
   tags: [one, two]  # Lists need brackets
   date: 2024-01-20  # Dates as strings
   ---
   ```

2. **Check delimiters**:
   ```markdown
   ---
   title: Correct
   ---
   
   Not this:
   ```
   ~~~
   title: Wrong
   ~~~
   ```

3. **Escape special characters**:
   ```yaml
   ---
   title: "Title: With Colon"  # Quote if contains :
   description: |  # Multi-line
     This is a long
     description
   ---
   ```

### Link Preservation Problems

**Symptoms:**
- Broken links in output
- Absolute paths not converted
- External links modified

**Solutions:**

1. **Enable link preservation**:
   ```yaml
   plugins:
     - output-as-input:
         preserve_links: true
   ```

2. **Understand link types**:
   - `/path` → `./path` (converted)
   - `https://` → `https://` (unchanged)
   - `//example.com` → `//example.com` (unchanged)
   - `path/file` → `path/file` (unchanged)

### Performance Issues

**Symptoms:**
- Slow builds
- High memory usage
- Timeouts on large sites

**Solutions:**

1. **Optimize configuration**:
   ```yaml
   plugins:
     - output-as-input:
         minify: true      # Faster than prettify
         verbose: false    # Reduce logging overhead
   ```

2. **Process in batches**:
   ```bash
   # Split large sites
   mkdocs build -f mkdocs-part1.yml
   mkdocs build -f mkdocs-part2.yml
   ```

3. **Exclude unnecessary files**:
   ```yaml
   # Use separate config for plugin
   docs_dir: docs_subset
   ```

## Error Messages

### "Cannot use both 'minify' and 'prettify'"

**Cause:** Mutually exclusive options enabled

**Solution:**
```yaml
plugins:
  - output-as-input:
      minify: true
      prettify: false  # Or remove this line
```

### "Failed to read HTML file"

**Cause:** File permissions or disk space

**Solutions:**
1. Check disk space: `df -h`
2. Check permissions: `ls -la site/`
3. Run as appropriate user

### "Failed to parse frontmatter"

**Cause:** Invalid YAML syntax

**Solution:** Use YAML validator:
```bash
python -c "import yaml; yaml.safe_load(open('docs/page.md').read().split('---')[1])"
```

## Platform-Specific Issues

### Windows

**Path separator issues:**
```yaml
# Use forward slashes
stage_dir: stage/output  # Correct
# NOT: stage\output
```

**Permission errors:**
- Run as Administrator
- Check antivirus exclusions

### macOS

**Case sensitivity:**
```yaml
# Be consistent with case
html_element: .md-content  # If class="md-content"
# NOT: .MD-Content
```

### Linux

**SELinux issues:**
```bash
# Check SELinux status
getenforce

# Temporary disable for testing
sudo setenforce 0
```

## Debug Techniques

### 1. Minimal Test Case

Create `test.md`:
```markdown
---
title: Test
---

# Test Content
```

Run with minimal config:
```bash
mkdocs new test_project
cd test_project
# Add plugin to mkdocs.yml
mkdocs build -v
```

### 2. Manual Processing

Test extraction manually:
```python
from bs4 import BeautifulSoup

with open('site/index.html') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    
# Test your selector
element = soup.select('.md-content')
print(f"Found: {len(element)} elements")
```

### 3. Build Logs Analysis

```bash
mkdocs build -v 2>&1 | tee build.log
grep -i "output.*input" build.log
```

### 4. Environment Info

Create debug script:
```python
import sys
import mkdocs
import mkdocs_output_as_input

print(f"Python: {sys.version}")
print(f"MkDocs: {mkdocs.__version__}")
print(f"Plugin: {mkdocs_output_as_input.__version__}")
```

## Getting Help

If you're still stuck:

1. **Gather information**:
   - MkDocs version
   - Plugin version
   - Python version
   - Minimal config that reproduces issue
   - Error messages/logs

2. **Search existing issues**:
   - [GitHub Issues](https://github.com/vexyart/vexy-mkdocs-output-as-input/issues)
   - Include closed issues

3. **Ask for help**:
   - [GitHub Discussions](https://github.com/vexyart/vexy-mkdocs-output-as-input/discussions)
   - Include all gathered information

4. **Report a bug**:
   - [New Issue](https://github.com/vexyart/vexy-mkdocs-output-as-input/issues/new)
   - Use issue template
   - Provide minimal reproduction

## Prevention Tips

1. **Keep dependencies updated**:
   ```bash
   pip install --upgrade mkdocs vexy-mkdocs-output-as-input
   ```

2. **Test configuration changes**:
   ```bash
   mkdocs build --strict
   ```

3. **Use version control**:
   - Track `mkdocs.yml` changes
   - Note when issues started

4. **Monitor build output**:
   - Set up CI/CD alerts
   - Check for warnings