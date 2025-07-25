---
description: Technical API documentation for the MkDocs Output as Input plugin
title: API Reference
---

<article class="md-main" data-md-component="main">
<div class="md-main__inner md-grid">
<div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation">
<div class="md-sidebar__scrollwrap">
<div class="md-sidebar__inner">
<nav aria-label="Navigation" class="md-nav md-nav--primary" data-md-level="0">
<label class="md-nav__title" for="__drawer">
<a aria-label="MkDocs Output as Input Plugin" class="md-nav__button md-logo" data-md-component="logo" href=".." title="MkDocs Output as Input Plugin">
<svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 8a3 3 0 0 0 3-3 3 3 0 0 0-3-3 3 3 0 0 0-3 3 3 3 0 0 0 3 3m0 3.54C9.64 9.35 6.5 8 3 8v11c3.5 0 6.64 1.35 9 3.54 2.36-2.19 5.5-3.54 9-3.54V8c-3.5 0-6.64 1.35-9 3.54"></path></svg>
</a>
    MkDocs Output as Input Plugin
  </label>
<div class="md-nav__source">
<a class="md-source" data-md-component="source" href="https://github.com/vexyart/vexy-mkdocs-output-as-input" title="Go to repository">
<div class="md-source__icon md-icon">
<svg viewbox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
</div>
<div class="md-source__repository">
    vexy-mkdocs-output-as-input
  </div>
</a>
</div>
<ul class="md-nav__list" data-md-scrollfix="">
<li class="md-nav__item">
<a class="md-nav__link" href="..">
<span class="md-ellipsis">
    Home
    
  </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="../getting-started/">
<span class="md-ellipsis">
    Getting Started
    
  </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="../configuration/">
<span class="md-ellipsis">
    Configuration
    
  </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="../examples/">
<span class="md-ellipsis">
    Examples
    
  </span>
</a>
</li>
<li class="md-nav__item md-nav__item--active">
<input class="md-nav__toggle md-toggle" id="__toc" type="checkbox"/>
<label class="md-nav__link md-nav__link--active" for="__toc">
<span class="md-ellipsis">
    API Reference
    
  </span>
<span class="md-nav__icon md-icon"></span>
</label>
<a class="md-nav__link md-nav__link--active" href="./">
<span class="md-ellipsis">
    API Reference
    
  </span>
</a>
<nav aria-label="Table of contents" class="md-nav md-nav--secondary">
<label class="md-nav__title" for="__toc">
<span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
<ul class="md-nav__list" data-md-component="toc" data-md-scrollfix="">
<li class="md-nav__item">
<a class="md-nav__link" href="#plugin-class">
<span class="md-ellipsis">
      Plugin Class
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin">
<span class="md-ellipsis">
<code class="doc-symbol doc-symbol-toc doc-symbol-class"></code> OutputAsInputPlugin
    </span>
</a>
<nav aria-label=" OutputAsInputPlugin" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin.config_scheme">
<span class="md-ellipsis">
<code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code> config_scheme
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin.on_page_read_source">
<span class="md-ellipsis">
<code class="doc-symbol doc-symbol-toc doc-symbol-method"></code> on_page_read_source
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin.on_post_build">
<span class="md-ellipsis">
<code class="doc-symbol doc-symbol-toc doc-symbol-method"></code> on_post_build
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#configuration-schema">
<span class="md-ellipsis">
      Configuration Schema
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#event-hooks">
<span class="md-ellipsis">
      Event Hooks
    </span>
</a>
<nav aria-label="Event Hooks" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#on_page_read_source">
<span class="md-ellipsis">
      on_page_read_source
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#on_post_build">
<span class="md-ellipsis">
      on_post_build
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#internal-methods">
<span class="md-ellipsis">
      Internal Methods
    </span>
</a>
<nav aria-label="Internal Methods" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#_extract_frontmattercontent-str-tupledict-str">
<span class="md-ellipsis">
      _extract_frontmatter(content: str) -&gt; tuple[dict, str]
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#_create_cousin_filesite_dir-str-rel_path-str-frontmatter-dict-html_content-str">
<span class="md-ellipsis">
      _create_cousin_file(site_dir: str, rel_path: str, frontmatter: dict, html_content: str)
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#data-storage">
<span class="md-ellipsis">
      Data Storage
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#error-handling">
<span class="md-ellipsis">
      Error Handling
    </span>
</a>
<nav aria-label="Error Handling" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#missing-html-element">
<span class="md-ellipsis">
      Missing HTML Element
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#invalid-frontmatter">
<span class="md-ellipsis">
      Invalid Frontmatter
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#file-io-errors">
<span class="md-ellipsis">
      File I/O Errors
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#usage-in-python">
<span class="md-ellipsis">
      Usage in Python
    </span>
</a>
<nav aria-label="Usage in Python" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#programmatic-usage">
<span class="md-ellipsis">
      Programmatic Usage
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#custom-integration">
<span class="md-ellipsis">
      Custom Integration
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#cli-tool">
<span class="md-ellipsis">
      CLI Tool
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.cli">
<span class="md-ellipsis">
      cli
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.cli.main">
<span class="md-ellipsis">
      main
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.cli.process_file">
<span class="md-ellipsis">
      process_file
    </span>
</a>
<nav aria-label="process_file" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#cli-usage">
<span class="md-ellipsis">
      CLI Usage
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#type-hints">
<span class="md-ellipsis">
      Type Hints
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#logging">
<span class="md-ellipsis">
      Logging
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#testing">
<span class="md-ellipsis">
      Testing
    </span>
</a>
</li>
</ul>
</nav>
</li>
</ul>
</nav>
</div>
</div>
</div>
<div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc">
<div class="md-sidebar__scrollwrap">
<div class="md-sidebar__inner">
<nav aria-label="Table of contents" class="md-nav md-nav--secondary">
<label class="md-nav__title" for="__toc">
<span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
<ul class="md-nav__list" data-md-component="toc" data-md-scrollfix="">
<li class="md-nav__item">
<a class="md-nav__link" href="#plugin-class">
<span class="md-ellipsis">
      Plugin Class
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin">
<span class="md-ellipsis">
<code class="doc-symbol doc-symbol-toc doc-symbol-class"></code> OutputAsInputPlugin
    </span>
</a>
<nav aria-label=" OutputAsInputPlugin" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin.config_scheme">
<span class="md-ellipsis">
<code class="doc-symbol doc-symbol-toc doc-symbol-attribute"></code> config_scheme
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin.on_page_read_source">
<span class="md-ellipsis">
<code class="doc-symbol doc-symbol-toc doc-symbol-method"></code> on_page_read_source
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin.on_post_build">
<span class="md-ellipsis">
<code class="doc-symbol doc-symbol-toc doc-symbol-method"></code> on_post_build
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#configuration-schema">
<span class="md-ellipsis">
      Configuration Schema
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#event-hooks">
<span class="md-ellipsis">
      Event Hooks
    </span>
</a>
<nav aria-label="Event Hooks" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#on_page_read_source">
<span class="md-ellipsis">
      on_page_read_source
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#on_post_build">
<span class="md-ellipsis">
      on_post_build
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#internal-methods">
<span class="md-ellipsis">
      Internal Methods
    </span>
</a>
<nav aria-label="Internal Methods" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#_extract_frontmattercontent-str-tupledict-str">
<span class="md-ellipsis">
      _extract_frontmatter(content: str) -&gt; tuple[dict, str]
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#_create_cousin_filesite_dir-str-rel_path-str-frontmatter-dict-html_content-str">
<span class="md-ellipsis">
      _create_cousin_file(site_dir: str, rel_path: str, frontmatter: dict, html_content: str)
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#data-storage">
<span class="md-ellipsis">
      Data Storage
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#error-handling">
<span class="md-ellipsis">
      Error Handling
    </span>
</a>
<nav aria-label="Error Handling" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#missing-html-element">
<span class="md-ellipsis">
      Missing HTML Element
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#invalid-frontmatter">
<span class="md-ellipsis">
      Invalid Frontmatter
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#file-io-errors">
<span class="md-ellipsis">
      File I/O Errors
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#usage-in-python">
<span class="md-ellipsis">
      Usage in Python
    </span>
</a>
<nav aria-label="Usage in Python" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#programmatic-usage">
<span class="md-ellipsis">
      Programmatic Usage
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#custom-integration">
<span class="md-ellipsis">
      Custom Integration
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#cli-tool">
<span class="md-ellipsis">
      CLI Tool
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.cli">
<span class="md-ellipsis">
      cli
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.cli.main">
<span class="md-ellipsis">
      main
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#mkdocs_output_as_input.cli.process_file">
<span class="md-ellipsis">
      process_file
    </span>
</a>
<nav aria-label="process_file" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#cli-usage">
<span class="md-ellipsis">
      CLI Usage
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#type-hints">
<span class="md-ellipsis">
      Type Hints
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#logging">
<span class="md-ellipsis">
      Logging
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#testing">
<span class="md-ellipsis">
      Testing
    </span>
</a>
</li>
</ul>
</nav>
</div>
</div>
</div>
<div class="md-content" data-md-component="content">
<article class="md-content__inner md-typeset">
<h1 id="api-reference">API Reference<a class="headerlink" href="#api-reference" title="Permanent link">¶</a></h1>
<p>This page provides detailed technical documentation for the MkDocs Output as Input plugin.</p>
<h2 id="plugin-class">Plugin Class<a class="headerlink" href="#plugin-class" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-class">
<h2 class="doc doc-heading" id="mkdocs_output_as_input.plugin.OutputAsInputPlugin">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <code>mkdocs_output_as_input.plugin.OutputAsInputPlugin</code>
<a class="headerlink" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin" title="Permanent link">¶</a></h2>
<div class="doc doc-contents first">
<p class="doc doc-class-bases">
              Bases: <code><span title="mkdocs.plugins.BasePlugin">BasePlugin</span></code></p>
<p>MkDocs plugin that captures HTML output and creates cousin Markdown files.</p>
<p>This plugin:
1. Lets the entire MkDocs build process run normally
2. Tracks all source Markdown files and their YAML frontmatter
3. After the build, creates a "stage" directory that replicates the source structure
4. For each source Markdown file, creates a cousin file with original frontmatter
   and extracted HTML</p>
<details class="quote">
<summary>Source code in <code>src/mkdocs_output_as_input/plugin.py</code></summary>
<div class="highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-22"> 22</a></span>
<span class="normal"><a href="#__codelineno-0-23"> 23</a></span>
<span class="normal"><a href="#__codelineno-0-24"> 24</a></span>
<span class="normal"><a href="#__codelineno-0-25"> 25</a></span>
<span class="normal"><a href="#__codelineno-0-26"> 26</a></span>
<span class="normal"><a href="#__codelineno-0-27"> 27</a></span>
<span class="normal"><a href="#__codelineno-0-28"> 28</a></span>
<span class="normal"><a href="#__codelineno-0-29"> 29</a></span>
<span class="normal"><a href="#__codelineno-0-30"> 30</a></span>
<span class="normal"><a href="#__codelineno-0-31"> 31</a></span>
<span class="normal"><a href="#__codelineno-0-32"> 32</a></span>
<span class="normal"><a href="#__codelineno-0-33"> 33</a></span>
<span class="normal"><a href="#__codelineno-0-34"> 34</a></span>
<span class="normal"><a href="#__codelineno-0-35"> 35</a></span>
<span class="normal"><a href="#__codelineno-0-36"> 36</a></span>
<span class="normal"><a href="#__codelineno-0-37"> 37</a></span>
<span class="normal"><a href="#__codelineno-0-38"> 38</a></span>
<span class="normal"><a href="#__codelineno-0-39"> 39</a></span>
<span class="normal"><a href="#__codelineno-0-40"> 40</a></span>
<span class="normal"><a href="#__codelineno-0-41"> 41</a></span>
<span class="normal"><a href="#__codelineno-0-42"> 42</a></span>
<span class="normal"><a href="#__codelineno-0-43"> 43</a></span>
<span class="normal"><a href="#__codelineno-0-44"> 44</a></span>
<span class="normal"><a href="#__codelineno-0-45"> 45</a></span>
<span class="normal"><a href="#__codelineno-0-46"> 46</a></span>
<span class="normal"><a href="#__codelineno-0-47"> 47</a></span>
<span class="normal"><a href="#__codelineno-0-48"> 48</a></span>
<span class="normal"><a href="#__codelineno-0-49"> 49</a></span>
<span class="normal"><a href="#__codelineno-0-50"> 50</a></span>
<span class="normal"><a href="#__codelineno-0-51"> 51</a></span>
<span class="normal"><a href="#__codelineno-0-52"> 52</a></span>
<span class="normal"><a href="#__codelineno-0-53"> 53</a></span>
<span class="normal"><a href="#__codelineno-0-54"> 54</a></span>
<span class="normal"><a href="#__codelineno-0-55"> 55</a></span>
<span class="normal"><a href="#__codelineno-0-56"> 56</a></span>
<span class="normal"><a href="#__codelineno-0-57"> 57</a></span>
<span class="normal"><a href="#__codelineno-0-58"> 58</a></span>
<span class="normal"><a href="#__codelineno-0-59"> 59</a></span>
<span class="normal"><a href="#__codelineno-0-60"> 60</a></span>
<span class="normal"><a href="#__codelineno-0-61"> 61</a></span>
<span class="normal"><a href="#__codelineno-0-62"> 62</a></span>
<span class="normal"><a href="#__codelineno-0-63"> 63</a></span>
<span class="normal"><a href="#__codelineno-0-64"> 64</a></span>
<span class="normal"><a href="#__codelineno-0-65"> 65</a></span>
<span class="normal"><a href="#__codelineno-0-66"> 66</a></span>
<span class="normal"><a href="#__codelineno-0-67"> 67</a></span>
<span class="normal"><a href="#__codelineno-0-68"> 68</a></span>
<span class="normal"><a href="#__codelineno-0-69"> 69</a></span>
<span class="normal"><a href="#__codelineno-0-70"> 70</a></span>
<span class="normal"><a href="#__codelineno-0-71"> 71</a></span>
<span class="normal"><a href="#__codelineno-0-72"> 72</a></span>
<span class="normal"><a href="#__codelineno-0-73"> 73</a></span>
<span class="normal"><a href="#__codelineno-0-74"> 74</a></span>
<span class="normal"><a href="#__codelineno-0-75"> 75</a></span>
<span class="normal"><a href="#__codelineno-0-76"> 76</a></span>
<span class="normal"><a href="#__codelineno-0-77"> 77</a></span>
<span class="normal"><a href="#__codelineno-0-78"> 78</a></span>
<span class="normal"><a href="#__codelineno-0-79"> 79</a></span>
<span class="normal"><a href="#__codelineno-0-80"> 80</a></span>
<span class="normal"><a href="#__codelineno-0-81"> 81</a></span>
<span class="normal"><a href="#__codelineno-0-82"> 82</a></span>
<span class="normal"><a href="#__codelineno-0-83"> 83</a></span>
<span class="normal"><a href="#__codelineno-0-84"> 84</a></span>
<span class="normal"><a href="#__codelineno-0-85"> 85</a></span>
<span class="normal"><a href="#__codelineno-0-86"> 86</a></span>
<span class="normal"><a href="#__codelineno-0-87"> 87</a></span>
<span class="normal"><a href="#__codelineno-0-88"> 88</a></span>
<span class="normal"><a href="#__codelineno-0-89"> 89</a></span>
<span class="normal"><a href="#__codelineno-0-90"> 90</a></span>
<span class="normal"><a href="#__codelineno-0-91"> 91</a></span>
<span class="normal"><a href="#__codelineno-0-92"> 92</a></span>
<span class="normal"><a href="#__codelineno-0-93"> 93</a></span>
<span class="normal"><a href="#__codelineno-0-94"> 94</a></span>
<span class="normal"><a href="#__codelineno-0-95"> 95</a></span>
<span class="normal"><a href="#__codelineno-0-96"> 96</a></span>
<span class="normal"><a href="#__codelineno-0-97"> 97</a></span>
<span class="normal"><a href="#__codelineno-0-98"> 98</a></span>
<span class="normal"><a href="#__codelineno-0-99"> 99</a></span>
<span class="normal"><a href="#__codelineno-0-100">100</a></span>
<span class="normal"><a href="#__codelineno-0-101">101</a></span>
<span class="normal"><a href="#__codelineno-0-102">102</a></span>
<span class="normal"><a href="#__codelineno-0-103">103</a></span>
<span class="normal"><a href="#__codelineno-0-104">104</a></span>
<span class="normal"><a href="#__codelineno-0-105">105</a></span>
<span class="normal"><a href="#__codelineno-0-106">106</a></span>
<span class="normal"><a href="#__codelineno-0-107">107</a></span>
<span class="normal"><a href="#__codelineno-0-108">108</a></span>
<span class="normal"><a href="#__codelineno-0-109">109</a></span>
<span class="normal"><a href="#__codelineno-0-110">110</a></span>
<span class="normal"><a href="#__codelineno-0-111">111</a></span>
<span class="normal"><a href="#__codelineno-0-112">112</a></span>
<span class="normal"><a href="#__codelineno-0-113">113</a></span>
<span class="normal"><a href="#__codelineno-0-114">114</a></span>
<span class="normal"><a href="#__codelineno-0-115">115</a></span>
<span class="normal"><a href="#__codelineno-0-116">116</a></span>
<span class="normal"><a href="#__codelineno-0-117">117</a></span>
<span class="normal"><a href="#__codelineno-0-118">118</a></span>
<span class="normal"><a href="#__codelineno-0-119">119</a></span>
<span class="normal"><a href="#__codelineno-0-120">120</a></span>
<span class="normal"><a href="#__codelineno-0-121">121</a></span>
<span class="normal"><a href="#__codelineno-0-122">122</a></span>
<span class="normal"><a href="#__codelineno-0-123">123</a></span>
<span class="normal"><a href="#__codelineno-0-124">124</a></span>
<span class="normal"><a href="#__codelineno-0-125">125</a></span>
<span class="normal"><a href="#__codelineno-0-126">126</a></span>
<span class="normal"><a href="#__codelineno-0-127">127</a></span>
<span class="normal"><a href="#__codelineno-0-128">128</a></span>
<span class="normal"><a href="#__codelineno-0-129">129</a></span>
<span class="normal"><a href="#__codelineno-0-130">130</a></span>
<span class="normal"><a href="#__codelineno-0-131">131</a></span>
<span class="normal"><a href="#__codelineno-0-132">132</a></span>
<span class="normal"><a href="#__codelineno-0-133">133</a></span>
<span class="normal"><a href="#__codelineno-0-134">134</a></span>
<span class="normal"><a href="#__codelineno-0-135">135</a></span>
<span class="normal"><a href="#__codelineno-0-136">136</a></span>
<span class="normal"><a href="#__codelineno-0-137">137</a></span>
<span class="normal"><a href="#__codelineno-0-138">138</a></span>
<span class="normal"><a href="#__codelineno-0-139">139</a></span>
<span class="normal"><a href="#__codelineno-0-140">140</a></span>
<span class="normal"><a href="#__codelineno-0-141">141</a></span>
<span class="normal"><a href="#__codelineno-0-142">142</a></span>
<span class="normal"><a href="#__codelineno-0-143">143</a></span>
<span class="normal"><a href="#__codelineno-0-144">144</a></span>
<span class="normal"><a href="#__codelineno-0-145">145</a></span>
<span class="normal"><a href="#__codelineno-0-146">146</a></span>
<span class="normal"><a href="#__codelineno-0-147">147</a></span>
<span class="normal"><a href="#__codelineno-0-148">148</a></span>
<span class="normal"><a href="#__codelineno-0-149">149</a></span>
<span class="normal"><a href="#__codelineno-0-150">150</a></span>
<span class="normal"><a href="#__codelineno-0-151">151</a></span>
<span class="normal"><a href="#__codelineno-0-152">152</a></span>
<span class="normal"><a href="#__codelineno-0-153">153</a></span>
<span class="normal"><a href="#__codelineno-0-154">154</a></span>
<span class="normal"><a href="#__codelineno-0-155">155</a></span>
<span class="normal"><a href="#__codelineno-0-156">156</a></span>
<span class="normal"><a href="#__codelineno-0-157">157</a></span>
<span class="normal"><a href="#__codelineno-0-158">158</a></span>
<span class="normal"><a href="#__codelineno-0-159">159</a></span>
<span class="normal"><a href="#__codelineno-0-160">160</a></span>
<span class="normal"><a href="#__codelineno-0-161">161</a></span>
<span class="normal"><a href="#__codelineno-0-162">162</a></span>
<span class="normal"><a href="#__codelineno-0-163">163</a></span>
<span class="normal"><a href="#__codelineno-0-164">164</a></span>
<span class="normal"><a href="#__codelineno-0-165">165</a></span>
<span class="normal"><a href="#__codelineno-0-166">166</a></span>
<span class="normal"><a href="#__codelineno-0-167">167</a></span>
<span class="normal"><a href="#__codelineno-0-168">168</a></span>
<span class="normal"><a href="#__codelineno-0-169">169</a></span>
<span class="normal"><a href="#__codelineno-0-170">170</a></span>
<span class="normal"><a href="#__codelineno-0-171">171</a></span>
<span class="normal"><a href="#__codelineno-0-172">172</a></span>
<span class="normal"><a href="#__codelineno-0-173">173</a></span>
<span class="normal"><a href="#__codelineno-0-174">174</a></span>
<span class="normal"><a href="#__codelineno-0-175">175</a></span>
<span class="normal"><a href="#__codelineno-0-176">176</a></span>
<span class="normal"><a href="#__codelineno-0-177">177</a></span>
<span class="normal"><a href="#__codelineno-0-178">178</a></span>
<span class="normal"><a href="#__codelineno-0-179">179</a></span>
<span class="normal"><a href="#__codelineno-0-180">180</a></span>
<span class="normal"><a href="#__codelineno-0-181">181</a></span>
<span class="normal"><a href="#__codelineno-0-182">182</a></span>
<span class="normal"><a href="#__codelineno-0-183">183</a></span>
<span class="normal"><a href="#__codelineno-0-184">184</a></span>
<span class="normal"><a href="#__codelineno-0-185">185</a></span>
<span class="normal"><a href="#__codelineno-0-186">186</a></span>
<span class="normal"><a href="#__codelineno-0-187">187</a></span>
<span class="normal"><a href="#__codelineno-0-188">188</a></span>
<span class="normal"><a href="#__codelineno-0-189">189</a></span>
<span class="normal"><a href="#__codelineno-0-190">190</a></span>
<span class="normal"><a href="#__codelineno-0-191">191</a></span>
<span class="normal"><a href="#__codelineno-0-192">192</a></span>
<span class="normal"><a href="#__codelineno-0-193">193</a></span>
<span class="normal"><a href="#__codelineno-0-194">194</a></span>
<span class="normal"><a href="#__codelineno-0-195">195</a></span>
<span class="normal"><a href="#__codelineno-0-196">196</a></span>
<span class="normal"><a href="#__codelineno-0-197">197</a></span>
<span class="normal"><a href="#__codelineno-0-198">198</a></span>
<span class="normal"><a href="#__codelineno-0-199">199</a></span>
<span class="normal"><a href="#__codelineno-0-200">200</a></span>
<span class="normal"><a href="#__codelineno-0-201">201</a></span>
<span class="normal"><a href="#__codelineno-0-202">202</a></span>
<span class="normal"><a href="#__codelineno-0-203">203</a></span>
<span class="normal"><a href="#__codelineno-0-204">204</a></span>
<span class="normal"><a href="#__codelineno-0-205">205</a></span>
<span class="normal"><a href="#__codelineno-0-206">206</a></span>
<span class="normal"><a href="#__codelineno-0-207">207</a></span>
<span class="normal"><a href="#__codelineno-0-208">208</a></span>
<span class="normal"><a href="#__codelineno-0-209">209</a></span>
<span class="normal"><a href="#__codelineno-0-210">210</a></span>
<span class="normal"><a href="#__codelineno-0-211">211</a></span>
<span class="normal"><a href="#__codelineno-0-212">212</a></span>
<span class="normal"><a href="#__codelineno-0-213">213</a></span>
<span class="normal"><a href="#__codelineno-0-214">214</a></span>
<span class="normal"><a href="#__codelineno-0-215">215</a></span>
<span class="normal"><a href="#__codelineno-0-216">216</a></span>
<span class="normal"><a href="#__codelineno-0-217">217</a></span>
<span class="normal"><a href="#__codelineno-0-218">218</a></span>
<span class="normal"><a href="#__codelineno-0-219">219</a></span>
<span class="normal"><a href="#__codelineno-0-220">220</a></span>
<span class="normal"><a href="#__codelineno-0-221">221</a></span>
<span class="normal"><a href="#__codelineno-0-222">222</a></span>
<span class="normal"><a href="#__codelineno-0-223">223</a></span>
<span class="normal"><a href="#__codelineno-0-224">224</a></span>
<span class="normal"><a href="#__codelineno-0-225">225</a></span>
<span class="normal"><a href="#__codelineno-0-226">226</a></span>
<span class="normal"><a href="#__codelineno-0-227">227</a></span>
<span class="normal"><a href="#__codelineno-0-228">228</a></span>
<span class="normal"><a href="#__codelineno-0-229">229</a></span>
<span class="normal"><a href="#__codelineno-0-230">230</a></span>
<span class="normal"><a href="#__codelineno-0-231">231</a></span>
<span class="normal"><a href="#__codelineno-0-232">232</a></span>
<span class="normal"><a href="#__codelineno-0-233">233</a></span>
<span class="normal"><a href="#__codelineno-0-234">234</a></span>
<span class="normal"><a href="#__codelineno-0-235">235</a></span>
<span class="normal"><a href="#__codelineno-0-236">236</a></span>
<span class="normal"><a href="#__codelineno-0-237">237</a></span>
<span class="normal"><a href="#__codelineno-0-238">238</a></span>
<span class="normal"><a href="#__codelineno-0-239">239</a></span>
<span class="normal"><a href="#__codelineno-0-240">240</a></span>
<span class="normal"><a href="#__codelineno-0-241">241</a></span>
<span class="normal"><a href="#__codelineno-0-242">242</a></span>
<span class="normal"><a href="#__codelineno-0-243">243</a></span>
<span class="normal"><a href="#__codelineno-0-244">244</a></span>
<span class="normal"><a href="#__codelineno-0-245">245</a></span>
<span class="normal"><a href="#__codelineno-0-246">246</a></span>
<span class="normal"><a href="#__codelineno-0-247">247</a></span>
<span class="normal"><a href="#__codelineno-0-248">248</a></span>
<span class="normal"><a href="#__codelineno-0-249">249</a></span>
<span class="normal"><a href="#__codelineno-0-250">250</a></span>
<span class="normal"><a href="#__codelineno-0-251">251</a></span>
<span class="normal"><a href="#__codelineno-0-252">252</a></span>
<span class="normal"><a href="#__codelineno-0-253">253</a></span>
<span class="normal"><a href="#__codelineno-0-254">254</a></span>
<span class="normal"><a href="#__codelineno-0-255">255</a></span>
<span class="normal"><a href="#__codelineno-0-256">256</a></span>
<span class="normal"><a href="#__codelineno-0-257">257</a></span>
<span class="normal"><a href="#__codelineno-0-258">258</a></span>
<span class="normal"><a href="#__codelineno-0-259">259</a></span>
<span class="normal"><a href="#__codelineno-0-260">260</a></span>
<span class="normal"><a href="#__codelineno-0-261">261</a></span>
<span class="normal"><a href="#__codelineno-0-262">262</a></span>
<span class="normal"><a href="#__codelineno-0-263">263</a></span>
<span class="normal"><a href="#__codelineno-0-264">264</a></span>
<span class="normal"><a href="#__codelineno-0-265">265</a></span>
<span class="normal"><a href="#__codelineno-0-266">266</a></span>
<span class="normal"><a href="#__codelineno-0-267">267</a></span>
<span class="normal"><a href="#__codelineno-0-268">268</a></span>
<span class="normal"><a href="#__codelineno-0-269">269</a></span>
<span class="normal"><a href="#__codelineno-0-270">270</a></span>
<span class="normal"><a href="#__codelineno-0-271">271</a></span>
<span class="normal"><a href="#__codelineno-0-272">272</a></span>
<span class="normal"><a href="#__codelineno-0-273">273</a></span>
<span class="normal"><a href="#__codelineno-0-274">274</a></span>
<span class="normal"><a href="#__codelineno-0-275">275</a></span>
<span class="normal"><a href="#__codelineno-0-276">276</a></span>
<span class="normal"><a href="#__codelineno-0-277">277</a></span>
<span class="normal"><a href="#__codelineno-0-278">278</a></span>
<span class="normal"><a href="#__codelineno-0-279">279</a></span>
<span class="normal"><a href="#__codelineno-0-280">280</a></span>
<span class="normal"><a href="#__codelineno-0-281">281</a></span>
<span class="normal"><a href="#__codelineno-0-282">282</a></span>
<span class="normal"><a href="#__codelineno-0-283">283</a></span>
<span class="normal"><a href="#__codelineno-0-284">284</a></span>
<span class="normal"><a href="#__codelineno-0-285">285</a></span>
<span class="normal"><a href="#__codelineno-0-286">286</a></span>
<span class="normal"><a href="#__codelineno-0-287">287</a></span>
<span class="normal"><a href="#__codelineno-0-288">288</a></span>
<span class="normal"><a href="#__codelineno-0-289">289</a></span>
<span class="normal"><a href="#__codelineno-0-290">290</a></span>
<span class="normal"><a href="#__codelineno-0-291">291</a></span>
<span class="normal"><a href="#__codelineno-0-292">292</a></span>
<span class="normal"><a href="#__codelineno-0-293">293</a></span>
<span class="normal"><a href="#__codelineno-0-294">294</a></span>
<span class="normal"><a href="#__codelineno-0-295">295</a></span>
<span class="normal"><a href="#__codelineno-0-296">296</a></span></pre></div></td><td class="code"><div><pre><span></span><code><a id="__codelineno-0-22" name="__codelineno-0-22"></a><span class="k">class</span><span class="w"> </span><span class="nc">OutputAsInputPlugin</span><span class="p">(</span><span class="n">BasePlugin</span><span class="p">):</span>  <span class="c1"># type: ignore[type-arg,no-untyped-call]</span>
<a id="__codelineno-0-23" name="__codelineno-0-23"></a><span class="w">    </span><span class="sd">"""MkDocs plugin that captures HTML output and creates cousin Markdown files.</span>
<a id="__codelineno-0-24" name="__codelineno-0-24"></a>
<a id="__codelineno-0-25" name="__codelineno-0-25"></a><span class="sd">    This plugin:</span>
<a id="__codelineno-0-26" name="__codelineno-0-26"></a><span class="sd">    1. Lets the entire MkDocs build process run normally</span>
<a id="__codelineno-0-27" name="__codelineno-0-27"></a><span class="sd">    2. Tracks all source Markdown files and their YAML frontmatter</span>
<a id="__codelineno-0-28" name="__codelineno-0-28"></a><span class="sd">    3. After the build, creates a "stage" directory that replicates the source structure</span>
<a id="__codelineno-0-29" name="__codelineno-0-29"></a><span class="sd">    4. For each source Markdown file, creates a cousin file with original frontmatter</span>
<a id="__codelineno-0-30" name="__codelineno-0-30"></a><span class="sd">       and extracted HTML</span>
<a id="__codelineno-0-31" name="__codelineno-0-31"></a><span class="sd">    """</span>
<a id="__codelineno-0-32" name="__codelineno-0-32"></a>
<a id="__codelineno-0-33" name="__codelineno-0-33"></a>    <span class="n">config_scheme</span> <span class="o">=</span> <span class="p">(</span>
<a id="__codelineno-0-34" name="__codelineno-0-34"></a>        <span class="p">(</span><span class="s2">"stage_dir"</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s2">"stage"</span><span class="p">)),</span>
<a id="__codelineno-0-35" name="__codelineno-0-35"></a>        <span class="p">(</span><span class="s2">"html_element"</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">((</span><span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">),</span> <span class="n">default</span><span class="o">=</span><span class="s2">"main"</span><span class="p">)),</span>
<a id="__codelineno-0-36" name="__codelineno-0-36"></a>        <span class="p">(</span><span class="s2">"target_tag"</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s2">"article"</span><span class="p">)),</span>
<a id="__codelineno-0-37" name="__codelineno-0-37"></a>        <span class="p">(</span><span class="s2">"include_frontmatter"</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">bool</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">True</span><span class="p">)),</span>
<a id="__codelineno-0-38" name="__codelineno-0-38"></a>        <span class="p">(</span><span class="s2">"preserve_links"</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">bool</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)),</span>
<a id="__codelineno-0-39" name="__codelineno-0-39"></a>        <span class="p">(</span><span class="s2">"minify"</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">bool</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)),</span>
<a id="__codelineno-0-40" name="__codelineno-0-40"></a>        <span class="p">(</span><span class="s2">"prettify"</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">bool</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)),</span>
<a id="__codelineno-0-41" name="__codelineno-0-41"></a>        <span class="p">(</span><span class="s2">"verbose"</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">bool</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)),</span>
<a id="__codelineno-0-42" name="__codelineno-0-42"></a>    <span class="p">)</span>
<a id="__codelineno-0-43" name="__codelineno-0-43"></a>
<a id="__codelineno-0-44" name="__codelineno-0-44"></a>    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<a id="__codelineno-0-45" name="__codelineno-0-45"></a><span class="w">        </span><span class="sd">"""Initialize the plugin."""</span>
<a id="__codelineno-0-46" name="__codelineno-0-46"></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
<a id="__codelineno-0-47" name="__codelineno-0-47"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">source_files</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">FileInfo</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
<a id="__codelineno-0-48" name="__codelineno-0-48"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">site_dir</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<a id="__codelineno-0-49" name="__codelineno-0-49"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">docs_dir</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<a id="__codelineno-0-50" name="__codelineno-0-50"></a>
<a id="__codelineno-0-51" name="__codelineno-0-51"></a>    <span class="k">def</span><span class="w"> </span><span class="nf">on_config</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">config</span><span class="p">:</span> <span class="n">ConfigDict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ConfigDict</span><span class="p">:</span>  <span class="c1"># type: ignore[override]</span>
<a id="__codelineno-0-52" name="__codelineno-0-52"></a><span class="w">        </span><span class="sd">"""Store site and docs directories and validate configuration.</span>
<a id="__codelineno-0-53" name="__codelineno-0-53"></a>
<a id="__codelineno-0-54" name="__codelineno-0-54"></a><span class="sd">        Args:</span>
<a id="__codelineno-0-55" name="__codelineno-0-55"></a><span class="sd">            config: MkDocs configuration dictionary</span>
<a id="__codelineno-0-56" name="__codelineno-0-56"></a>
<a id="__codelineno-0-57" name="__codelineno-0-57"></a><span class="sd">        Returns:</span>
<a id="__codelineno-0-58" name="__codelineno-0-58"></a><span class="sd">            The unmodified configuration dictionary</span>
<a id="__codelineno-0-59" name="__codelineno-0-59"></a>
<a id="__codelineno-0-60" name="__codelineno-0-60"></a><span class="sd">        Raises:</span>
<a id="__codelineno-0-61" name="__codelineno-0-61"></a><span class="sd">            ValueError: If mutually exclusive options are enabled</span>
<a id="__codelineno-0-62" name="__codelineno-0-62"></a><span class="sd">        """</span>
<a id="__codelineno-0-63" name="__codelineno-0-63"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">site_dir</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">config</span><span class="p">[</span><span class="s2">"site_dir"</span><span class="p">])</span>
<a id="__codelineno-0-64" name="__codelineno-0-64"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">docs_dir</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">config</span><span class="p">[</span><span class="s2">"docs_dir"</span><span class="p">])</span>
<a id="__codelineno-0-65" name="__codelineno-0-65"></a>
<a id="__codelineno-0-66" name="__codelineno-0-66"></a>        <span class="c1"># Validate mutually exclusive options</span>
<a id="__codelineno-0-67" name="__codelineno-0-67"></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"minify"</span><span class="p">]</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"prettify"</span><span class="p">]:</span>
<a id="__codelineno-0-68" name="__codelineno-0-68"></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Cannot use both 'minify' and 'prettify' options"</span><span class="p">)</span>
<a id="__codelineno-0-69" name="__codelineno-0-69"></a>
<a id="__codelineno-0-70" name="__codelineno-0-70"></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"verbose"</span><span class="p">]:</span>
<a id="__codelineno-0-71" name="__codelineno-0-71"></a>            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Plugin initialized"</span><span class="p">,</span> <span class="n">site_dir</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">site_dir</span><span class="p">,</span> <span class="n">docs_dir</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">docs_dir</span><span class="p">)</span>
<a id="__codelineno-0-72" name="__codelineno-0-72"></a>            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Configuration"</span><span class="p">,</span> <span class="n">config</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">)</span>
<a id="__codelineno-0-73" name="__codelineno-0-73"></a>
<a id="__codelineno-0-74" name="__codelineno-0-74"></a>        <span class="k">return</span> <span class="n">config</span>
<a id="__codelineno-0-75" name="__codelineno-0-75"></a>
<a id="__codelineno-0-76" name="__codelineno-0-76"></a>    <span class="k">def</span><span class="w"> </span><span class="nf">on_page_read_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">page</span><span class="p">:</span> <span class="n">Page</span><span class="p">,</span> <span class="n">config</span><span class="p">:</span> <span class="n">ConfigDict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># type: ignore[override]  # noqa: ARG002</span>
<a id="__codelineno-0-77" name="__codelineno-0-77"></a><span class="w">        </span><span class="sd">"""Capture source Markdown content and frontmatter.</span>
<a id="__codelineno-0-78" name="__codelineno-0-78"></a>
<a id="__codelineno-0-79" name="__codelineno-0-79"></a><span class="sd">        Args:</span>
<a id="__codelineno-0-80" name="__codelineno-0-80"></a><span class="sd">            page: MkDocs page object</span>
<a id="__codelineno-0-81" name="__codelineno-0-81"></a><span class="sd">            config: MkDocs configuration dictionary</span>
<a id="__codelineno-0-82" name="__codelineno-0-82"></a>
<a id="__codelineno-0-83" name="__codelineno-0-83"></a><span class="sd">        Returns:</span>
<a id="__codelineno-0-84" name="__codelineno-0-84"></a><span class="sd">            None to let MkDocs continue with original content</span>
<a id="__codelineno-0-85" name="__codelineno-0-85"></a><span class="sd">        """</span>
<a id="__codelineno-0-86" name="__codelineno-0-86"></a>        <span class="n">src_path</span> <span class="o">=</span> <span class="n">page</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">src_path</span>
<a id="__codelineno-0-87" name="__codelineno-0-87"></a>        <span class="n">start_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
<a id="__codelineno-0-88" name="__codelineno-0-88"></a>
<a id="__codelineno-0-89" name="__codelineno-0-89"></a>        <span class="c1"># Read the full source content</span>
<a id="__codelineno-0-90" name="__codelineno-0-90"></a>        <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-91" name="__codelineno-0-91"></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">page</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">abs_src_path</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>  <span class="c1"># type: ignore[arg-type]</span>
<a id="__codelineno-0-92" name="__codelineno-0-92"></a>                <span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
<a id="__codelineno-0-93" name="__codelineno-0-93"></a>        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-94" name="__codelineno-0-94"></a>            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"Failed to read source file"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">src_path</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
<a id="__codelineno-0-95" name="__codelineno-0-95"></a>            <span class="k">return</span> <span class="kc">None</span>
<a id="__codelineno-0-96" name="__codelineno-0-96"></a>
<a id="__codelineno-0-97" name="__codelineno-0-97"></a>        <span class="c1"># Extract frontmatter if present</span>
<a id="__codelineno-0-98" name="__codelineno-0-98"></a>        <span class="n">frontmatter</span><span class="p">:</span> <span class="n">FrontmatterDict</span> <span class="o">=</span> <span class="p">{}</span>
<a id="__codelineno-0-99" name="__codelineno-0-99"></a>        <span class="k">if</span> <span class="n">content</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"---</span><span class="se">\n</span><span class="s2">"</span><span class="p">):</span>
<a id="__codelineno-0-100" name="__codelineno-0-100"></a>            <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-101" name="__codelineno-0-101"></a>                <span class="n">end_idx</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">---</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>
<a id="__codelineno-0-102" name="__codelineno-0-102"></a>                <span class="k">if</span> <span class="n">end_idx</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
<a id="__codelineno-0-103" name="__codelineno-0-103"></a>                    <span class="n">fm_text</span> <span class="o">=</span> <span class="n">content</span><span class="p">[</span><span class="mi">4</span><span class="p">:</span><span class="n">end_idx</span><span class="p">]</span>
<a id="__codelineno-0-104" name="__codelineno-0-104"></a>                    <span class="n">frontmatter</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">fm_text</span><span class="p">)</span> <span class="ow">or</span> <span class="p">{}</span>
<a id="__codelineno-0-105" name="__codelineno-0-105"></a>            <span class="k">except</span> <span class="n">yaml</span><span class="o">.</span><span class="n">YAMLError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-106" name="__codelineno-0-106"></a>                <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">"Failed to parse frontmatter"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">src_path</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
<a id="__codelineno-0-107" name="__codelineno-0-107"></a>
<a id="__codelineno-0-108" name="__codelineno-0-108"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">source_files</span><span class="p">[</span><span class="n">src_path</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
<a id="__codelineno-0-109" name="__codelineno-0-109"></a>            <span class="s2">"frontmatter"</span><span class="p">:</span> <span class="n">frontmatter</span><span class="p">,</span>
<a id="__codelineno-0-110" name="__codelineno-0-110"></a>            <span class="s2">"abs_src_path"</span><span class="p">:</span> <span class="n">page</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">abs_src_path</span><span class="p">,</span>
<a id="__codelineno-0-111" name="__codelineno-0-111"></a>        <span class="p">}</span>
<a id="__codelineno-0-112" name="__codelineno-0-112"></a>
<a id="__codelineno-0-113" name="__codelineno-0-113"></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"verbose"</span><span class="p">]:</span>
<a id="__codelineno-0-114" name="__codelineno-0-114"></a>            <span class="n">elapsed</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span>
<a id="__codelineno-0-115" name="__codelineno-0-115"></a>            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
<a id="__codelineno-0-116" name="__codelineno-0-116"></a>                <span class="s2">"Captured source file"</span><span class="p">,</span>
<a id="__codelineno-0-117" name="__codelineno-0-117"></a>                <span class="n">path</span><span class="o">=</span><span class="n">src_path</span><span class="p">,</span>
<a id="__codelineno-0-118" name="__codelineno-0-118"></a>                <span class="n">frontmatter_keys</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="n">frontmatter</span><span class="o">.</span><span class="n">keys</span><span class="p">()),</span>
<a id="__codelineno-0-119" name="__codelineno-0-119"></a>                <span class="n">elapsed_ms</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">elapsed</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1000</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span>
<a id="__codelineno-0-120" name="__codelineno-0-120"></a>            <span class="p">)</span>
<a id="__codelineno-0-121" name="__codelineno-0-121"></a>
<a id="__codelineno-0-122" name="__codelineno-0-122"></a>        <span class="k">return</span> <span class="kc">None</span>  <span class="c1"># Let MkDocs continue with original content</span>
<a id="__codelineno-0-123" name="__codelineno-0-123"></a>
<a id="__codelineno-0-124" name="__codelineno-0-124"></a>    <span class="k">def</span><span class="w"> </span><span class="nf">on_post_build</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">config</span><span class="p">:</span> <span class="n">ConfigDict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># type: ignore[override]  # noqa: ARG002</span>
<a id="__codelineno-0-125" name="__codelineno-0-125"></a><span class="w">        </span><span class="sd">"""After build, process all HTML files and create cousin Markdowns.</span>
<a id="__codelineno-0-126" name="__codelineno-0-126"></a>
<a id="__codelineno-0-127" name="__codelineno-0-127"></a><span class="sd">        Args:</span>
<a id="__codelineno-0-128" name="__codelineno-0-128"></a><span class="sd">            config: MkDocs configuration dictionary</span>
<a id="__codelineno-0-129" name="__codelineno-0-129"></a><span class="sd">        """</span>
<a id="__codelineno-0-130" name="__codelineno-0-130"></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">docs_dir</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
<a id="__codelineno-0-131" name="__codelineno-0-131"></a>            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"docs_dir not set, cannot process files"</span><span class="p">)</span>
<a id="__codelineno-0-132" name="__codelineno-0-132"></a>            <span class="k">return</span>
<a id="__codelineno-0-133" name="__codelineno-0-133"></a>
<a id="__codelineno-0-134" name="__codelineno-0-134"></a>        <span class="n">start_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
<a id="__codelineno-0-135" name="__codelineno-0-135"></a>        <span class="n">stage_dir</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docs_dir</span><span class="o">.</span><span class="n">parent</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"stage_dir"</span><span class="p">]</span>
<a id="__codelineno-0-136" name="__codelineno-0-136"></a>
<a id="__codelineno-0-137" name="__codelineno-0-137"></a>        <span class="c1"># Create stage directory</span>
<a id="__codelineno-0-138" name="__codelineno-0-138"></a>        <span class="n">stage_dir</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="n">exist_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<a id="__codelineno-0-139" name="__codelineno-0-139"></a>        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Creating stage directory"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">stage_dir</span><span class="p">)</span>
<a id="__codelineno-0-140" name="__codelineno-0-140"></a>
<a id="__codelineno-0-141" name="__codelineno-0-141"></a>        <span class="c1"># Process each tracked source file</span>
<a id="__codelineno-0-142" name="__codelineno-0-142"></a>        <span class="n">processed</span> <span class="o">=</span> <span class="mi">0</span>
<a id="__codelineno-0-143" name="__codelineno-0-143"></a>        <span class="n">failed</span> <span class="o">=</span> <span class="mi">0</span>
<a id="__codelineno-0-144" name="__codelineno-0-144"></a>
<a id="__codelineno-0-145" name="__codelineno-0-145"></a>        <span class="k">with</span> <span class="n">logger</span><span class="o">.</span><span class="n">contextualize</span><span class="p">(</span><span class="n">stage_dir</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">stage_dir</span><span class="p">)):</span>
<a id="__codelineno-0-146" name="__codelineno-0-146"></a>            <span class="k">for</span> <span class="n">src_path</span><span class="p">,</span> <span class="n">file_info</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">source_files</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
<a id="__codelineno-0-147" name="__codelineno-0-147"></a>                <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-148" name="__codelineno-0-148"></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_process_file</span><span class="p">(</span><span class="n">src_path</span><span class="p">,</span> <span class="n">file_info</span><span class="p">,</span> <span class="n">stage_dir</span><span class="p">)</span>
<a id="__codelineno-0-149" name="__codelineno-0-149"></a>                    <span class="n">processed</span> <span class="o">+=</span> <span class="mi">1</span>
<a id="__codelineno-0-150" name="__codelineno-0-150"></a>                <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-151" name="__codelineno-0-151"></a>                    <span class="n">failed</span> <span class="o">+=</span> <span class="mi">1</span>
<a id="__codelineno-0-152" name="__codelineno-0-152"></a>                    <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
<a id="__codelineno-0-153" name="__codelineno-0-153"></a>                        <span class="s2">"Failed to process file"</span><span class="p">,</span>
<a id="__codelineno-0-154" name="__codelineno-0-154"></a>                        <span class="n">path</span><span class="o">=</span><span class="n">src_path</span><span class="p">,</span>
<a id="__codelineno-0-155" name="__codelineno-0-155"></a>                        <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">),</span>
<a id="__codelineno-0-156" name="__codelineno-0-156"></a>                        <span class="n">exc_info</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"verbose"</span><span class="p">]</span>
<a id="__codelineno-0-157" name="__codelineno-0-157"></a>                    <span class="p">)</span>
<a id="__codelineno-0-158" name="__codelineno-0-158"></a>
<a id="__codelineno-0-159" name="__codelineno-0-159"></a>        <span class="n">elapsed</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span>
<a id="__codelineno-0-160" name="__codelineno-0-160"></a>        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
<a id="__codelineno-0-161" name="__codelineno-0-161"></a>            <span class="s2">"Post-build processing complete"</span><span class="p">,</span>
<a id="__codelineno-0-162" name="__codelineno-0-162"></a>            <span class="n">processed</span><span class="o">=</span><span class="n">processed</span><span class="p">,</span>
<a id="__codelineno-0-163" name="__codelineno-0-163"></a>            <span class="n">failed</span><span class="o">=</span><span class="n">failed</span><span class="p">,</span>
<a id="__codelineno-0-164" name="__codelineno-0-164"></a>            <span class="n">total</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">source_files</span><span class="p">),</span>
<a id="__codelineno-0-165" name="__codelineno-0-165"></a>            <span class="n">elapsed_s</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">elapsed</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span>
<a id="__codelineno-0-166" name="__codelineno-0-166"></a>        <span class="p">)</span>
<a id="__codelineno-0-167" name="__codelineno-0-167"></a>
<a id="__codelineno-0-168" name="__codelineno-0-168"></a>    <span class="k">def</span><span class="w"> </span><span class="nf">_process_file</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">src_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_info</span><span class="p">:</span> <span class="n">FileInfo</span><span class="p">,</span> <span class="n">stage_dir</span><span class="p">:</span> <span class="n">Path</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<a id="__codelineno-0-169" name="__codelineno-0-169"></a><span class="w">        </span><span class="sd">"""Process a single file: extract HTML and create cousin Markdown.</span>
<a id="__codelineno-0-170" name="__codelineno-0-170"></a>
<a id="__codelineno-0-171" name="__codelineno-0-171"></a><span class="sd">        Args:</span>
<a id="__codelineno-0-172" name="__codelineno-0-172"></a><span class="sd">            src_path: Path to the source Markdown file</span>
<a id="__codelineno-0-173" name="__codelineno-0-173"></a><span class="sd">            file_info: Dictionary containing file metadata and frontmatter</span>
<a id="__codelineno-0-174" name="__codelineno-0-174"></a><span class="sd">            stage_dir: Directory where cousin files will be created</span>
<a id="__codelineno-0-175" name="__codelineno-0-175"></a><span class="sd">        """</span>
<a id="__codelineno-0-176" name="__codelineno-0-176"></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">site_dir</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
<a id="__codelineno-0-177" name="__codelineno-0-177"></a>            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"site_dir not set"</span><span class="p">)</span>
<a id="__codelineno-0-178" name="__codelineno-0-178"></a>            <span class="k">return</span>
<a id="__codelineno-0-179" name="__codelineno-0-179"></a>
<a id="__codelineno-0-180" name="__codelineno-0-180"></a>        <span class="c1"># Determine HTML output path</span>
<a id="__codelineno-0-181" name="__codelineno-0-181"></a>        <span class="c1"># Special case: README.md often becomes index.html at root</span>
<a id="__codelineno-0-182" name="__codelineno-0-182"></a>        <span class="k">if</span> <span class="n">src_path</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o">==</span> <span class="s2">"readme.md"</span><span class="p">:</span>
<a id="__codelineno-0-183" name="__codelineno-0-183"></a>            <span class="n">html_path</span> <span class="o">=</span> <span class="s2">"index.html"</span>
<a id="__codelineno-0-184" name="__codelineno-0-184"></a>            <span class="n">full_html_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">site_dir</span> <span class="o">/</span> <span class="n">html_path</span>
<a id="__codelineno-0-185" name="__codelineno-0-185"></a>        <span class="k">else</span><span class="p">:</span>
<a id="__codelineno-0-186" name="__codelineno-0-186"></a>            <span class="n">html_path</span> <span class="o">=</span> <span class="n">src_path</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">".md"</span><span class="p">,</span> <span class="s2">"/index.html"</span><span class="p">)</span>
<a id="__codelineno-0-187" name="__codelineno-0-187"></a>            <span class="n">full_html_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">site_dir</span> <span class="o">/</span> <span class="n">html_path</span>
<a id="__codelineno-0-188" name="__codelineno-0-188"></a>
<a id="__codelineno-0-189" name="__codelineno-0-189"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">full_html_path</span><span class="o">.</span><span class="n">exists</span><span class="p">():</span>
<a id="__codelineno-0-190" name="__codelineno-0-190"></a>            <span class="c1"># Try without the index.html suffix</span>
<a id="__codelineno-0-191" name="__codelineno-0-191"></a>            <span class="n">html_path</span> <span class="o">=</span> <span class="n">src_path</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">".md"</span><span class="p">,</span> <span class="s2">".html"</span><span class="p">)</span>
<a id="__codelineno-0-192" name="__codelineno-0-192"></a>            <span class="n">full_html_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">site_dir</span> <span class="o">/</span> <span class="n">html_path</span>
<a id="__codelineno-0-193" name="__codelineno-0-193"></a>
<a id="__codelineno-0-194" name="__codelineno-0-194"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">full_html_path</span><span class="o">.</span><span class="n">exists</span><span class="p">():</span>
<a id="__codelineno-0-195" name="__codelineno-0-195"></a>            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
<a id="__codelineno-0-196" name="__codelineno-0-196"></a>                <span class="s2">"No HTML output found"</span><span class="p">,</span>
<a id="__codelineno-0-197" name="__codelineno-0-197"></a>                <span class="n">source</span><span class="o">=</span><span class="n">src_path</span><span class="p">,</span>
<a id="__codelineno-0-198" name="__codelineno-0-198"></a>                <span class="n">expected_path</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">full_html_path</span><span class="p">)</span>
<a id="__codelineno-0-199" name="__codelineno-0-199"></a>            <span class="p">)</span>
<a id="__codelineno-0-200" name="__codelineno-0-200"></a>            <span class="k">return</span>
<a id="__codelineno-0-201" name="__codelineno-0-201"></a>
<a id="__codelineno-0-202" name="__codelineno-0-202"></a>        <span class="c1"># Read and parse HTML</span>
<a id="__codelineno-0-203" name="__codelineno-0-203"></a>        <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-204" name="__codelineno-0-204"></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">full_html_path</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
<a id="__codelineno-0-205" name="__codelineno-0-205"></a>                <span class="n">html_content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
<a id="__codelineno-0-206" name="__codelineno-0-206"></a>        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-207" name="__codelineno-0-207"></a>            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"Failed to read HTML file"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">full_html_path</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
<a id="__codelineno-0-208" name="__codelineno-0-208"></a>            <span class="k">return</span>
<a id="__codelineno-0-209" name="__codelineno-0-209"></a>
<a id="__codelineno-0-210" name="__codelineno-0-210"></a>        <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">html_content</span><span class="p">,</span> <span class="s2">"html.parser"</span><span class="p">)</span>
<a id="__codelineno-0-211" name="__codelineno-0-211"></a>
<a id="__codelineno-0-212" name="__codelineno-0-212"></a>        <span class="c1"># Extract target element(s)</span>
<a id="__codelineno-0-213" name="__codelineno-0-213"></a>        <span class="n">html_elements</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"html_element"</span><span class="p">]</span>
<a id="__codelineno-0-214" name="__codelineno-0-214"></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">html_elements</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
<a id="__codelineno-0-215" name="__codelineno-0-215"></a>            <span class="n">html_elements</span> <span class="o">=</span> <span class="p">[</span><span class="n">html_elements</span><span class="p">]</span>
<a id="__codelineno-0-216" name="__codelineno-0-216"></a>
<a id="__codelineno-0-217" name="__codelineno-0-217"></a>        <span class="n">extracted_elements</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
<a id="__codelineno-0-218" name="__codelineno-0-218"></a>        <span class="k">for</span> <span class="n">selector</span> <span class="ow">in</span> <span class="n">html_elements</span><span class="p">:</span>
<a id="__codelineno-0-219" name="__codelineno-0-219"></a>            <span class="c1"># Try CSS selector first</span>
<a id="__codelineno-0-220" name="__codelineno-0-220"></a>            <span class="n">elements</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="n">selector</span><span class="p">)</span>
<a id="__codelineno-0-221" name="__codelineno-0-221"></a>            <span class="k">if</span> <span class="n">elements</span><span class="p">:</span>
<a id="__codelineno-0-222" name="__codelineno-0-222"></a>                <span class="n">extracted_elements</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span>
<a id="__codelineno-0-223" name="__codelineno-0-223"></a>            <span class="k">else</span><span class="p">:</span>
<a id="__codelineno-0-224" name="__codelineno-0-224"></a>                <span class="c1"># Fall back to tag name</span>
<a id="__codelineno-0-225" name="__codelineno-0-225"></a>                <span class="n">element</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">selector</span><span class="p">)</span>
<a id="__codelineno-0-226" name="__codelineno-0-226"></a>                <span class="k">if</span> <span class="n">element</span><span class="p">:</span>
<a id="__codelineno-0-227" name="__codelineno-0-227"></a>                    <span class="n">extracted_elements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">element</span><span class="p">)</span>
<a id="__codelineno-0-228" name="__codelineno-0-228"></a>
<a id="__codelineno-0-229" name="__codelineno-0-229"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">extracted_elements</span><span class="p">:</span>
<a id="__codelineno-0-230" name="__codelineno-0-230"></a>            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
<a id="__codelineno-0-231" name="__codelineno-0-231"></a>                <span class="s2">"No matching elements found"</span><span class="p">,</span>
<a id="__codelineno-0-232" name="__codelineno-0-232"></a>                <span class="n">selectors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s1">'html_element'</span><span class="p">],</span>
<a id="__codelineno-0-233" name="__codelineno-0-233"></a>                <span class="n">html_file</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">full_html_path</span><span class="p">)</span>
<a id="__codelineno-0-234" name="__codelineno-0-234"></a>            <span class="p">)</span>
<a id="__codelineno-0-235" name="__codelineno-0-235"></a>            <span class="k">return</span>
<a id="__codelineno-0-236" name="__codelineno-0-236"></a>
<a id="__codelineno-0-237" name="__codelineno-0-237"></a>        <span class="c1"># If multiple elements, wrap them in a container</span>
<a id="__codelineno-0-238" name="__codelineno-0-238"></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">extracted_elements</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
<a id="__codelineno-0-239" name="__codelineno-0-239"></a>            <span class="n">container</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">new_tag</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"target_tag"</span><span class="p">])</span>
<a id="__codelineno-0-240" name="__codelineno-0-240"></a>            <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">extracted_elements</span><span class="p">:</span>
<a id="__codelineno-0-241" name="__codelineno-0-241"></a>                <span class="n">container</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elem</span><span class="o">.</span><span class="n">extract</span><span class="p">())</span>
<a id="__codelineno-0-242" name="__codelineno-0-242"></a>            <span class="n">target_element</span> <span class="o">=</span> <span class="n">container</span>
<a id="__codelineno-0-243" name="__codelineno-0-243"></a>        <span class="k">else</span><span class="p">:</span>
<a id="__codelineno-0-244" name="__codelineno-0-244"></a>            <span class="n">target_element</span> <span class="o">=</span> <span class="n">extracted_elements</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># type: ignore[assignment]</span>
<a id="__codelineno-0-245" name="__codelineno-0-245"></a>            <span class="c1"># Transform to target tag if different and single selector was a tag name</span>
<a id="__codelineno-0-246" name="__codelineno-0-246"></a>            <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"html_element"</span><span class="p">],</span> <span class="nb">str</span><span class="p">)</span> <span class="ow">and</span> 
<a id="__codelineno-0-247" name="__codelineno-0-247"></a>                <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"target_tag"</span><span class="p">]</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"html_element"</span><span class="p">]):</span>
<a id="__codelineno-0-248" name="__codelineno-0-248"></a>                <span class="n">target_element</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"target_tag"</span><span class="p">]</span>
<a id="__codelineno-0-249" name="__codelineno-0-249"></a>
<a id="__codelineno-0-250" name="__codelineno-0-250"></a>        <span class="c1"># Handle link preservation if requested</span>
<a id="__codelineno-0-251" name="__codelineno-0-251"></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"preserve_links"</span><span class="p">]:</span>
<a id="__codelineno-0-252" name="__codelineno-0-252"></a>            <span class="c1"># Convert absolute links back to relative</span>
<a id="__codelineno-0-253" name="__codelineno-0-253"></a>            <span class="k">for</span> <span class="n">link</span> <span class="ow">in</span> <span class="n">target_element</span><span class="o">.</span><span class="n">find_all</span><span class="p">([</span><span class="s2">"a"</span><span class="p">,</span> <span class="s2">"img"</span><span class="p">,</span> <span class="s2">"link"</span><span class="p">,</span> <span class="s2">"script"</span><span class="p">]):</span>
<a id="__codelineno-0-254" name="__codelineno-0-254"></a>                <span class="k">for</span> <span class="n">attr</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"href"</span><span class="p">,</span> <span class="s2">"src"</span><span class="p">]:</span>
<a id="__codelineno-0-255" name="__codelineno-0-255"></a>                    <span class="k">if</span> <span class="n">link</span><span class="o">.</span><span class="n">has_attr</span><span class="p">(</span><span class="n">attr</span><span class="p">):</span>
<a id="__codelineno-0-256" name="__codelineno-0-256"></a>                        <span class="n">url</span> <span class="o">=</span> <span class="n">link</span><span class="p">[</span><span class="n">attr</span><span class="p">]</span>
<a id="__codelineno-0-257" name="__codelineno-0-257"></a>                        <span class="c1"># Simple heuristic: if it starts with /, it's likely a root-relative link</span>
<a id="__codelineno-0-258" name="__codelineno-0-258"></a>                        <span class="c1"># In a real implementation, this would be more sophisticated</span>
<a id="__codelineno-0-259" name="__codelineno-0-259"></a>                        <span class="k">if</span> <span class="n">url</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"/"</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">url</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"//"</span><span class="p">):</span>
<a id="__codelineno-0-260" name="__codelineno-0-260"></a>                            <span class="n">link</span><span class="p">[</span><span class="n">attr</span><span class="p">]</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">".</span><span class="si">{</span><span class="n">url</span><span class="si">}</span><span class="s2">"</span>
<a id="__codelineno-0-261" name="__codelineno-0-261"></a>
<a id="__codelineno-0-262" name="__codelineno-0-262"></a>        <span class="c1"># Create cousin file path</span>
<a id="__codelineno-0-263" name="__codelineno-0-263"></a>        <span class="n">cousin_path</span> <span class="o">=</span> <span class="n">stage_dir</span> <span class="o">/</span> <span class="n">src_path</span>
<a id="__codelineno-0-264" name="__codelineno-0-264"></a>        <span class="n">cousin_path</span><span class="o">.</span><span class="n">parent</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="n">parents</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">exist_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<a id="__codelineno-0-265" name="__codelineno-0-265"></a>
<a id="__codelineno-0-266" name="__codelineno-0-266"></a>        <span class="c1"># Write cousin file</span>
<a id="__codelineno-0-267" name="__codelineno-0-267"></a>        <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-268" name="__codelineno-0-268"></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">cousin_path</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
<a id="__codelineno-0-269" name="__codelineno-0-269"></a>                <span class="c1"># Write frontmatter if present and configured to include it</span>
<a id="__codelineno-0-270" name="__codelineno-0-270"></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"include_frontmatter"</span><span class="p">]</span> <span class="ow">and</span> <span class="n">file_info</span><span class="p">[</span><span class="s2">"frontmatter"</span><span class="p">]:</span>
<a id="__codelineno-0-271" name="__codelineno-0-271"></a>                    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">"---</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<a id="__codelineno-0-272" name="__codelineno-0-272"></a>                    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">yaml</span><span class="o">.</span><span class="n">safe_dump</span><span class="p">(</span><span class="n">file_info</span><span class="p">[</span><span class="s2">"frontmatter"</span><span class="p">],</span> <span class="n">default_flow_style</span><span class="o">=</span><span class="kc">False</span><span class="p">))</span>
<a id="__codelineno-0-273" name="__codelineno-0-273"></a>                    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">"---</span><span class="se">\n\n</span><span class="s2">"</span><span class="p">)</span>
<a id="__codelineno-0-274" name="__codelineno-0-274"></a>
<a id="__codelineno-0-275" name="__codelineno-0-275"></a>                <span class="c1"># Write extracted HTML with formatting options</span>
<a id="__codelineno-0-276" name="__codelineno-0-276"></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"minify"</span><span class="p">]:</span>
<a id="__codelineno-0-277" name="__codelineno-0-277"></a>                    <span class="c1"># Remove extra whitespace between tags</span>
<a id="__codelineno-0-278" name="__codelineno-0-278"></a>                    <span class="n">html_output</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">target_element</span><span class="p">)</span>
<a id="__codelineno-0-279" name="__codelineno-0-279"></a>                    <span class="c1"># Remove newlines and compress multiple spaces</span>
<a id="__codelineno-0-280" name="__codelineno-0-280"></a>                    <span class="n">html_output</span> <span class="o">=</span> <span class="n">html_output</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
<a id="__codelineno-0-281" name="__codelineno-0-281"></a>                    <span class="n">html_output</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s1">'\s+'</span><span class="p">,</span> <span class="s1">' '</span><span class="p">,</span> <span class="n">html_output</span><span class="p">)</span>
<a id="__codelineno-0-282" name="__codelineno-0-282"></a>                    <span class="c1"># Remove spaces between tags</span>
<a id="__codelineno-0-283" name="__codelineno-0-283"></a>                    <span class="n">html_output</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s1">'&gt;\s+&lt;'</span><span class="p">,</span> <span class="s1">'&gt;&lt;'</span><span class="p">,</span> <span class="n">html_output</span><span class="p">)</span>
<a id="__codelineno-0-284" name="__codelineno-0-284"></a>                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"prettify"</span><span class="p">]:</span>
<a id="__codelineno-0-285" name="__codelineno-0-285"></a>                    <span class="n">html_output</span> <span class="o">=</span> <span class="n">target_element</span><span class="o">.</span><span class="n">prettify</span><span class="p">()</span>
<a id="__codelineno-0-286" name="__codelineno-0-286"></a>                <span class="k">else</span><span class="p">:</span>
<a id="__codelineno-0-287" name="__codelineno-0-287"></a>                    <span class="n">html_output</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">target_element</span><span class="p">)</span>
<a id="__codelineno-0-288" name="__codelineno-0-288"></a>
<a id="__codelineno-0-289" name="__codelineno-0-289"></a>                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">html_output</span><span class="p">)</span>
<a id="__codelineno-0-290" name="__codelineno-0-290"></a>                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<a id="__codelineno-0-291" name="__codelineno-0-291"></a>
<a id="__codelineno-0-292" name="__codelineno-0-292"></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"verbose"</span><span class="p">]:</span>
<a id="__codelineno-0-293" name="__codelineno-0-293"></a>                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Created cousin file"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">cousin_path</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="n">cousin_path</span><span class="o">.</span><span class="n">stat</span><span class="p">()</span><span class="o">.</span><span class="n">st_size</span><span class="p">)</span>
<a id="__codelineno-0-294" name="__codelineno-0-294"></a>
<a id="__codelineno-0-295" name="__codelineno-0-295"></a>        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-296" name="__codelineno-0-296"></a>            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"Failed to write cousin file"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">cousin_path</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
</code></pre></div></td></tr></table></div>
</details>
<div class="doc doc-children">
<div class="doc doc-object doc-attribute">
<h3 class="doc doc-heading" id="mkdocs_output_as_input.plugin.OutputAsInputPlugin.config_scheme">
<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code> <code class="highlight language-python"><span class="n">config_scheme</span> <span class="o">=</span> <span class="p">((</span><span class="s1">'stage_dir'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s1">'stage'</span><span class="p">)),</span> <span class="p">(</span><span class="s1">'html_element'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">((</span><span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">),</span> <span class="n">default</span><span class="o">=</span><span class="s1">'main'</span><span class="p">)),</span> <span class="p">(</span><span class="s1">'target_tag'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s1">'article'</span><span class="p">)),</span> <span class="p">(</span><span class="s1">'include_frontmatter'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">bool</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">True</span><span class="p">)),</span> <span class="p">(</span><span class="s1">'preserve_links'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">bool</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)),</span> <span class="p">(</span><span class="s1">'minify'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">bool</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)),</span> <span class="p">(</span><span class="s1">'prettify'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">bool</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)),</span> <span class="p">(</span><span class="s1">'verbose'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">bool</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)))</span></code>
<span class="doc doc-labels">
<small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
<small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
</span>
<a class="headerlink" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin.config_scheme" title="Permanent link">¶</a></h3>
<div class="doc doc-contents">
</div>
</div>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="mkdocs_output_as_input.plugin.OutputAsInputPlugin.on_page_read_source">
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code> <code class="highlight language-python"><span class="n">on_page_read_source</span><span class="p">(</span><span class="n">page</span><span class="p">,</span> <span class="n">config</span><span class="p">)</span></code>
<a class="headerlink" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin.on_page_read_source" title="Permanent link">¶</a></h3>
<div class="doc doc-contents">
<p>Capture source Markdown content and frontmatter.</p>
<p><span class="doc-section-title">Parameters:</span></p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="doc-section-item">
<td>
<code>page</code>
</td>
<td>
<code><span title="mkdocs.structure.pages.Page">Page</span></code>
</td>
<td>
<div class="doc-md-description">
<p>MkDocs page object</p>
</div>
</td>
<td>
<em>required</em>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>config</code>
</td>
<td>
<code><span title="ConfigDict">ConfigDict</span></code>
</td>
<td>
<div class="doc-md-description">
<p>MkDocs configuration dictionary</p>
</div>
</td>
<td>
<em>required</em>
</td>
</tr>
</tbody>
</table>
<p><span class="doc-section-title">Returns:</span></p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="doc-section-item">
<td>
<code><span title="str">str</span> | None</code>
</td>
<td>
<div class="doc-md-description">
<p>None to let MkDocs continue with original content</p>
</div>
</td>
</tr>
</tbody>
</table>
<details class="quote">
<summary>Source code in <code>src/mkdocs_output_as_input/plugin.py</code></summary>
<div class="highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-76"> 76</a></span>
<span class="normal"><a href="#__codelineno-0-77"> 77</a></span>
<span class="normal"><a href="#__codelineno-0-78"> 78</a></span>
<span class="normal"><a href="#__codelineno-0-79"> 79</a></span>
<span class="normal"><a href="#__codelineno-0-80"> 80</a></span>
<span class="normal"><a href="#__codelineno-0-81"> 81</a></span>
<span class="normal"><a href="#__codelineno-0-82"> 82</a></span>
<span class="normal"><a href="#__codelineno-0-83"> 83</a></span>
<span class="normal"><a href="#__codelineno-0-84"> 84</a></span>
<span class="normal"><a href="#__codelineno-0-85"> 85</a></span>
<span class="normal"><a href="#__codelineno-0-86"> 86</a></span>
<span class="normal"><a href="#__codelineno-0-87"> 87</a></span>
<span class="normal"><a href="#__codelineno-0-88"> 88</a></span>
<span class="normal"><a href="#__codelineno-0-89"> 89</a></span>
<span class="normal"><a href="#__codelineno-0-90"> 90</a></span>
<span class="normal"><a href="#__codelineno-0-91"> 91</a></span>
<span class="normal"><a href="#__codelineno-0-92"> 92</a></span>
<span class="normal"><a href="#__codelineno-0-93"> 93</a></span>
<span class="normal"><a href="#__codelineno-0-94"> 94</a></span>
<span class="normal"><a href="#__codelineno-0-95"> 95</a></span>
<span class="normal"><a href="#__codelineno-0-96"> 96</a></span>
<span class="normal"><a href="#__codelineno-0-97"> 97</a></span>
<span class="normal"><a href="#__codelineno-0-98"> 98</a></span>
<span class="normal"><a href="#__codelineno-0-99"> 99</a></span>
<span class="normal"><a href="#__codelineno-0-100">100</a></span>
<span class="normal"><a href="#__codelineno-0-101">101</a></span>
<span class="normal"><a href="#__codelineno-0-102">102</a></span>
<span class="normal"><a href="#__codelineno-0-103">103</a></span>
<span class="normal"><a href="#__codelineno-0-104">104</a></span>
<span class="normal"><a href="#__codelineno-0-105">105</a></span>
<span class="normal"><a href="#__codelineno-0-106">106</a></span>
<span class="normal"><a href="#__codelineno-0-107">107</a></span>
<span class="normal"><a href="#__codelineno-0-108">108</a></span>
<span class="normal"><a href="#__codelineno-0-109">109</a></span>
<span class="normal"><a href="#__codelineno-0-110">110</a></span>
<span class="normal"><a href="#__codelineno-0-111">111</a></span>
<span class="normal"><a href="#__codelineno-0-112">112</a></span>
<span class="normal"><a href="#__codelineno-0-113">113</a></span>
<span class="normal"><a href="#__codelineno-0-114">114</a></span>
<span class="normal"><a href="#__codelineno-0-115">115</a></span>
<span class="normal"><a href="#__codelineno-0-116">116</a></span>
<span class="normal"><a href="#__codelineno-0-117">117</a></span>
<span class="normal"><a href="#__codelineno-0-118">118</a></span>
<span class="normal"><a href="#__codelineno-0-119">119</a></span>
<span class="normal"><a href="#__codelineno-0-120">120</a></span>
<span class="normal"><a href="#__codelineno-0-121">121</a></span>
<span class="normal"><a href="#__codelineno-0-122">122</a></span></pre></div></td><td class="code"><div><pre><span></span><code><a id="__codelineno-0-76" name="__codelineno-0-76"></a><span class="k">def</span><span class="w"> </span><span class="nf">on_page_read_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">page</span><span class="p">:</span> <span class="n">Page</span><span class="p">,</span> <span class="n">config</span><span class="p">:</span> <span class="n">ConfigDict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># type: ignore[override]  # noqa: ARG002</span>
<a id="__codelineno-0-77" name="__codelineno-0-77"></a><span class="w">    </span><span class="sd">"""Capture source Markdown content and frontmatter.</span>
<a id="__codelineno-0-78" name="__codelineno-0-78"></a>
<a id="__codelineno-0-79" name="__codelineno-0-79"></a><span class="sd">    Args:</span>
<a id="__codelineno-0-80" name="__codelineno-0-80"></a><span class="sd">        page: MkDocs page object</span>
<a id="__codelineno-0-81" name="__codelineno-0-81"></a><span class="sd">        config: MkDocs configuration dictionary</span>
<a id="__codelineno-0-82" name="__codelineno-0-82"></a>
<a id="__codelineno-0-83" name="__codelineno-0-83"></a><span class="sd">    Returns:</span>
<a id="__codelineno-0-84" name="__codelineno-0-84"></a><span class="sd">        None to let MkDocs continue with original content</span>
<a id="__codelineno-0-85" name="__codelineno-0-85"></a><span class="sd">    """</span>
<a id="__codelineno-0-86" name="__codelineno-0-86"></a>    <span class="n">src_path</span> <span class="o">=</span> <span class="n">page</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">src_path</span>
<a id="__codelineno-0-87" name="__codelineno-0-87"></a>    <span class="n">start_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
<a id="__codelineno-0-88" name="__codelineno-0-88"></a>
<a id="__codelineno-0-89" name="__codelineno-0-89"></a>    <span class="c1"># Read the full source content</span>
<a id="__codelineno-0-90" name="__codelineno-0-90"></a>    <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-91" name="__codelineno-0-91"></a>        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">page</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">abs_src_path</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>  <span class="c1"># type: ignore[arg-type]</span>
<a id="__codelineno-0-92" name="__codelineno-0-92"></a>            <span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
<a id="__codelineno-0-93" name="__codelineno-0-93"></a>    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-94" name="__codelineno-0-94"></a>        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"Failed to read source file"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">src_path</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
<a id="__codelineno-0-95" name="__codelineno-0-95"></a>        <span class="k">return</span> <span class="kc">None</span>
<a id="__codelineno-0-96" name="__codelineno-0-96"></a>
<a id="__codelineno-0-97" name="__codelineno-0-97"></a>    <span class="c1"># Extract frontmatter if present</span>
<a id="__codelineno-0-98" name="__codelineno-0-98"></a>    <span class="n">frontmatter</span><span class="p">:</span> <span class="n">FrontmatterDict</span> <span class="o">=</span> <span class="p">{}</span>
<a id="__codelineno-0-99" name="__codelineno-0-99"></a>    <span class="k">if</span> <span class="n">content</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"---</span><span class="se">\n</span><span class="s2">"</span><span class="p">):</span>
<a id="__codelineno-0-100" name="__codelineno-0-100"></a>        <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-101" name="__codelineno-0-101"></a>            <span class="n">end_idx</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">---</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>
<a id="__codelineno-0-102" name="__codelineno-0-102"></a>            <span class="k">if</span> <span class="n">end_idx</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
<a id="__codelineno-0-103" name="__codelineno-0-103"></a>                <span class="n">fm_text</span> <span class="o">=</span> <span class="n">content</span><span class="p">[</span><span class="mi">4</span><span class="p">:</span><span class="n">end_idx</span><span class="p">]</span>
<a id="__codelineno-0-104" name="__codelineno-0-104"></a>                <span class="n">frontmatter</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">fm_text</span><span class="p">)</span> <span class="ow">or</span> <span class="p">{}</span>
<a id="__codelineno-0-105" name="__codelineno-0-105"></a>        <span class="k">except</span> <span class="n">yaml</span><span class="o">.</span><span class="n">YAMLError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-106" name="__codelineno-0-106"></a>            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">"Failed to parse frontmatter"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">src_path</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
<a id="__codelineno-0-107" name="__codelineno-0-107"></a>
<a id="__codelineno-0-108" name="__codelineno-0-108"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">source_files</span><span class="p">[</span><span class="n">src_path</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
<a id="__codelineno-0-109" name="__codelineno-0-109"></a>        <span class="s2">"frontmatter"</span><span class="p">:</span> <span class="n">frontmatter</span><span class="p">,</span>
<a id="__codelineno-0-110" name="__codelineno-0-110"></a>        <span class="s2">"abs_src_path"</span><span class="p">:</span> <span class="n">page</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">abs_src_path</span><span class="p">,</span>
<a id="__codelineno-0-111" name="__codelineno-0-111"></a>    <span class="p">}</span>
<a id="__codelineno-0-112" name="__codelineno-0-112"></a>
<a id="__codelineno-0-113" name="__codelineno-0-113"></a>    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"verbose"</span><span class="p">]:</span>
<a id="__codelineno-0-114" name="__codelineno-0-114"></a>        <span class="n">elapsed</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span>
<a id="__codelineno-0-115" name="__codelineno-0-115"></a>        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
<a id="__codelineno-0-116" name="__codelineno-0-116"></a>            <span class="s2">"Captured source file"</span><span class="p">,</span>
<a id="__codelineno-0-117" name="__codelineno-0-117"></a>            <span class="n">path</span><span class="o">=</span><span class="n">src_path</span><span class="p">,</span>
<a id="__codelineno-0-118" name="__codelineno-0-118"></a>            <span class="n">frontmatter_keys</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="n">frontmatter</span><span class="o">.</span><span class="n">keys</span><span class="p">()),</span>
<a id="__codelineno-0-119" name="__codelineno-0-119"></a>            <span class="n">elapsed_ms</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">elapsed</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1000</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span>
<a id="__codelineno-0-120" name="__codelineno-0-120"></a>        <span class="p">)</span>
<a id="__codelineno-0-121" name="__codelineno-0-121"></a>
<a id="__codelineno-0-122" name="__codelineno-0-122"></a>    <span class="k">return</span> <span class="kc">None</span>  <span class="c1"># Let MkDocs continue with original content</span>
</code></pre></div></td></tr></table></div>
</details>
</div>
</div>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="mkdocs_output_as_input.plugin.OutputAsInputPlugin.on_post_build">
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code> <code class="highlight language-python"><span class="n">on_post_build</span><span class="p">(</span><span class="n">config</span><span class="p">)</span></code>
<a class="headerlink" href="#mkdocs_output_as_input.plugin.OutputAsInputPlugin.on_post_build" title="Permanent link">¶</a></h3>
<div class="doc doc-contents">
<p>After build, process all HTML files and create cousin Markdowns.</p>
<p><span class="doc-section-title">Parameters:</span></p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="doc-section-item">
<td>
<code>config</code>
</td>
<td>
<code><span title="ConfigDict">ConfigDict</span></code>
</td>
<td>
<div class="doc-md-description">
<p>MkDocs configuration dictionary</p>
</div>
</td>
<td>
<em>required</em>
</td>
</tr>
</tbody>
</table>
<details class="quote">
<summary>Source code in <code>src/mkdocs_output_as_input/plugin.py</code></summary>
<div class="highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-124">124</a></span>
<span class="normal"><a href="#__codelineno-0-125">125</a></span>
<span class="normal"><a href="#__codelineno-0-126">126</a></span>
<span class="normal"><a href="#__codelineno-0-127">127</a></span>
<span class="normal"><a href="#__codelineno-0-128">128</a></span>
<span class="normal"><a href="#__codelineno-0-129">129</a></span>
<span class="normal"><a href="#__codelineno-0-130">130</a></span>
<span class="normal"><a href="#__codelineno-0-131">131</a></span>
<span class="normal"><a href="#__codelineno-0-132">132</a></span>
<span class="normal"><a href="#__codelineno-0-133">133</a></span>
<span class="normal"><a href="#__codelineno-0-134">134</a></span>
<span class="normal"><a href="#__codelineno-0-135">135</a></span>
<span class="normal"><a href="#__codelineno-0-136">136</a></span>
<span class="normal"><a href="#__codelineno-0-137">137</a></span>
<span class="normal"><a href="#__codelineno-0-138">138</a></span>
<span class="normal"><a href="#__codelineno-0-139">139</a></span>
<span class="normal"><a href="#__codelineno-0-140">140</a></span>
<span class="normal"><a href="#__codelineno-0-141">141</a></span>
<span class="normal"><a href="#__codelineno-0-142">142</a></span>
<span class="normal"><a href="#__codelineno-0-143">143</a></span>
<span class="normal"><a href="#__codelineno-0-144">144</a></span>
<span class="normal"><a href="#__codelineno-0-145">145</a></span>
<span class="normal"><a href="#__codelineno-0-146">146</a></span>
<span class="normal"><a href="#__codelineno-0-147">147</a></span>
<span class="normal"><a href="#__codelineno-0-148">148</a></span>
<span class="normal"><a href="#__codelineno-0-149">149</a></span>
<span class="normal"><a href="#__codelineno-0-150">150</a></span>
<span class="normal"><a href="#__codelineno-0-151">151</a></span>
<span class="normal"><a href="#__codelineno-0-152">152</a></span>
<span class="normal"><a href="#__codelineno-0-153">153</a></span>
<span class="normal"><a href="#__codelineno-0-154">154</a></span>
<span class="normal"><a href="#__codelineno-0-155">155</a></span>
<span class="normal"><a href="#__codelineno-0-156">156</a></span>
<span class="normal"><a href="#__codelineno-0-157">157</a></span>
<span class="normal"><a href="#__codelineno-0-158">158</a></span>
<span class="normal"><a href="#__codelineno-0-159">159</a></span>
<span class="normal"><a href="#__codelineno-0-160">160</a></span>
<span class="normal"><a href="#__codelineno-0-161">161</a></span>
<span class="normal"><a href="#__codelineno-0-162">162</a></span>
<span class="normal"><a href="#__codelineno-0-163">163</a></span>
<span class="normal"><a href="#__codelineno-0-164">164</a></span>
<span class="normal"><a href="#__codelineno-0-165">165</a></span>
<span class="normal"><a href="#__codelineno-0-166">166</a></span></pre></div></td><td class="code"><div><pre><span></span><code><a id="__codelineno-0-124" name="__codelineno-0-124"></a><span class="k">def</span><span class="w"> </span><span class="nf">on_post_build</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">config</span><span class="p">:</span> <span class="n">ConfigDict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># type: ignore[override]  # noqa: ARG002</span>
<a id="__codelineno-0-125" name="__codelineno-0-125"></a><span class="w">    </span><span class="sd">"""After build, process all HTML files and create cousin Markdowns.</span>
<a id="__codelineno-0-126" name="__codelineno-0-126"></a>
<a id="__codelineno-0-127" name="__codelineno-0-127"></a><span class="sd">    Args:</span>
<a id="__codelineno-0-128" name="__codelineno-0-128"></a><span class="sd">        config: MkDocs configuration dictionary</span>
<a id="__codelineno-0-129" name="__codelineno-0-129"></a><span class="sd">    """</span>
<a id="__codelineno-0-130" name="__codelineno-0-130"></a>    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">docs_dir</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
<a id="__codelineno-0-131" name="__codelineno-0-131"></a>        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"docs_dir not set, cannot process files"</span><span class="p">)</span>
<a id="__codelineno-0-132" name="__codelineno-0-132"></a>        <span class="k">return</span>
<a id="__codelineno-0-133" name="__codelineno-0-133"></a>
<a id="__codelineno-0-134" name="__codelineno-0-134"></a>    <span class="n">start_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
<a id="__codelineno-0-135" name="__codelineno-0-135"></a>    <span class="n">stage_dir</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docs_dir</span><span class="o">.</span><span class="n">parent</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"stage_dir"</span><span class="p">]</span>
<a id="__codelineno-0-136" name="__codelineno-0-136"></a>
<a id="__codelineno-0-137" name="__codelineno-0-137"></a>    <span class="c1"># Create stage directory</span>
<a id="__codelineno-0-138" name="__codelineno-0-138"></a>    <span class="n">stage_dir</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="n">exist_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<a id="__codelineno-0-139" name="__codelineno-0-139"></a>    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Creating stage directory"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">stage_dir</span><span class="p">)</span>
<a id="__codelineno-0-140" name="__codelineno-0-140"></a>
<a id="__codelineno-0-141" name="__codelineno-0-141"></a>    <span class="c1"># Process each tracked source file</span>
<a id="__codelineno-0-142" name="__codelineno-0-142"></a>    <span class="n">processed</span> <span class="o">=</span> <span class="mi">0</span>
<a id="__codelineno-0-143" name="__codelineno-0-143"></a>    <span class="n">failed</span> <span class="o">=</span> <span class="mi">0</span>
<a id="__codelineno-0-144" name="__codelineno-0-144"></a>
<a id="__codelineno-0-145" name="__codelineno-0-145"></a>    <span class="k">with</span> <span class="n">logger</span><span class="o">.</span><span class="n">contextualize</span><span class="p">(</span><span class="n">stage_dir</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">stage_dir</span><span class="p">)):</span>
<a id="__codelineno-0-146" name="__codelineno-0-146"></a>        <span class="k">for</span> <span class="n">src_path</span><span class="p">,</span> <span class="n">file_info</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">source_files</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
<a id="__codelineno-0-147" name="__codelineno-0-147"></a>            <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-148" name="__codelineno-0-148"></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_process_file</span><span class="p">(</span><span class="n">src_path</span><span class="p">,</span> <span class="n">file_info</span><span class="p">,</span> <span class="n">stage_dir</span><span class="p">)</span>
<a id="__codelineno-0-149" name="__codelineno-0-149"></a>                <span class="n">processed</span> <span class="o">+=</span> <span class="mi">1</span>
<a id="__codelineno-0-150" name="__codelineno-0-150"></a>            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-151" name="__codelineno-0-151"></a>                <span class="n">failed</span> <span class="o">+=</span> <span class="mi">1</span>
<a id="__codelineno-0-152" name="__codelineno-0-152"></a>                <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
<a id="__codelineno-0-153" name="__codelineno-0-153"></a>                    <span class="s2">"Failed to process file"</span><span class="p">,</span>
<a id="__codelineno-0-154" name="__codelineno-0-154"></a>                    <span class="n">path</span><span class="o">=</span><span class="n">src_path</span><span class="p">,</span>
<a id="__codelineno-0-155" name="__codelineno-0-155"></a>                    <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">),</span>
<a id="__codelineno-0-156" name="__codelineno-0-156"></a>                    <span class="n">exc_info</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s2">"verbose"</span><span class="p">]</span>
<a id="__codelineno-0-157" name="__codelineno-0-157"></a>                <span class="p">)</span>
<a id="__codelineno-0-158" name="__codelineno-0-158"></a>
<a id="__codelineno-0-159" name="__codelineno-0-159"></a>    <span class="n">elapsed</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span>
<a id="__codelineno-0-160" name="__codelineno-0-160"></a>    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
<a id="__codelineno-0-161" name="__codelineno-0-161"></a>        <span class="s2">"Post-build processing complete"</span><span class="p">,</span>
<a id="__codelineno-0-162" name="__codelineno-0-162"></a>        <span class="n">processed</span><span class="o">=</span><span class="n">processed</span><span class="p">,</span>
<a id="__codelineno-0-163" name="__codelineno-0-163"></a>        <span class="n">failed</span><span class="o">=</span><span class="n">failed</span><span class="p">,</span>
<a id="__codelineno-0-164" name="__codelineno-0-164"></a>        <span class="n">total</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">source_files</span><span class="p">),</span>
<a id="__codelineno-0-165" name="__codelineno-0-165"></a>        <span class="n">elapsed_s</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">elapsed</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span>
<a id="__codelineno-0-166" name="__codelineno-0-166"></a>    <span class="p">)</span>
</code></pre></div></td></tr></table></div>
</details>
</div>
</div>
</div>
</div>
</div><h2 id="configuration-schema">Configuration Schema<a class="headerlink" href="#configuration-schema" title="Permanent link">¶</a></h2>
<p>The plugin uses MkDocs' configuration validation system:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">mkdocs.config</span><span class="w"> </span><span class="kn">import</span> <span class="n">config_options</span>
<a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">mkdocs.plugins</span><span class="w"> </span><span class="kn">import</span> <span class="n">BasePlugin</span>
<a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>
<a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a><span class="k">class</span><span class="w"> </span><span class="nc">OutputAsInputPlugin</span><span class="p">(</span><span class="n">BasePlugin</span><span class="p">):</span>
<a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a>    <span class="n">config_scheme</span> <span class="o">=</span> <span class="p">(</span>
<a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a>        <span class="p">(</span><span class="s1">'stage_dir'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s1">'stage'</span><span class="p">)),</span>
<a href="#__codelineno-0-7" id="__codelineno-0-7" name="__codelineno-0-7"></a>        <span class="p">(</span><span class="s1">'html_element'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s1">'main'</span><span class="p">)),</span>
<a href="#__codelineno-0-8" id="__codelineno-0-8" name="__codelineno-0-8"></a>        <span class="p">(</span><span class="s1">'target_tag'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s1">'article'</span><span class="p">)),</span>
<a href="#__codelineno-0-9" id="__codelineno-0-9" name="__codelineno-0-9"></a>        <span class="p">(</span><span class="s1">'verbose'</span><span class="p">,</span> <span class="n">config_options</span><span class="o">.</span><span class="n">Type</span><span class="p">(</span><span class="nb">bool</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)),</span>
<a href="#__codelineno-0-10" id="__codelineno-0-10" name="__codelineno-0-10"></a>    <span class="p">)</span>
</code></pre></div>
<h2 id="event-hooks">Event Hooks<a class="headerlink" href="#event-hooks" title="Permanent link">¶</a></h2>
<h3 id="on_page_read_source"><code>on_page_read_source</code><a class="headerlink" href="#on_page_read_source" title="Permanent link">¶</a></h3>
<p>Called when MkDocs reads a source file. The plugin uses this to capture frontmatter.</p>
<p><strong>Parameters:</strong>
- <code>page</code> - The MkDocs Page object
- <code>config</code> - The MkDocs configuration</p>
<p><strong>Returns:</strong>
- The original page content (unmodified)</p>
<p><strong>Behavior:</strong>
1. Extracts YAML frontmatter from the source file
2. Stores source path and frontmatter for later use
3. Handles parsing errors gracefully</p>
<h3 id="on_post_build"><code>on_post_build</code><a class="headerlink" href="#on_post_build" title="Permanent link">¶</a></h3>
<p>Called after MkDocs completes the build. This is where cousin files are created.</p>
<p><strong>Parameters:</strong>
- <code>config</code> - The MkDocs configuration</p>
<p><strong>Behavior:</strong>
1. Creates the stage directory if needed
2. Processes each HTML file in the site directory
3. Extracts content using BeautifulSoup
4. Creates cousin Markdown files with frontmatter + HTML</p>
<h2 id="internal-methods">Internal Methods<a class="headerlink" href="#internal-methods" title="Permanent link">¶</a></h2>
<h3 id="_extract_frontmattercontent-str-tupledict-str"><code>_extract_frontmatter(content: str) -&gt; tuple[dict, str]</code><a class="headerlink" href="#_extract_frontmattercontent-str-tupledict-str" title="Permanent link">¶</a></h3>
<p>Extracts YAML frontmatter from Markdown content.</p>
<p><strong>Parameters:</strong>
- <code>content</code> - Raw Markdown file content</p>
<p><strong>Returns:</strong>
- Tuple of (frontmatter_dict, remaining_content)</p>
<p><strong>Example:</strong>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="n">frontmatter</span><span class="p">,</span> <span class="n">content</span> <span class="o">=</span> <span class="n">plugin</span><span class="o">.</span><span class="n">_extract_frontmatter</span><span class="p">(</span><span class="s2">"""---</span>
<a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a><span class="s2">title: My Page</span>
<a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a><span class="s2">tags: [python, mkdocs]</span>
<a href="#__codelineno-1-4" id="__codelineno-1-4" name="__codelineno-1-4"></a><span class="s2">---</span>
<a href="#__codelineno-1-5" id="__codelineno-1-5" name="__codelineno-1-5"></a>
<a href="#__codelineno-1-6" id="__codelineno-1-6" name="__codelineno-1-6"></a><span class="s2"># Content here</span>
<a href="#__codelineno-1-7" id="__codelineno-1-7" name="__codelineno-1-7"></a><span class="s2">"""</span><span class="p">)</span>
<a href="#__codelineno-1-8" id="__codelineno-1-8" name="__codelineno-1-8"></a><span class="c1"># frontmatter = {'title': 'My Page', 'tags': ['python', 'mkdocs']}</span>
<a href="#__codelineno-1-9" id="__codelineno-1-9" name="__codelineno-1-9"></a><span class="c1"># content = "\n# Content here\n"</span>
</code></pre></div></p>
<h3 id="_create_cousin_filesite_dir-str-rel_path-str-frontmatter-dict-html_content-str"><code>_create_cousin_file(site_dir: str, rel_path: str, frontmatter: dict, html_content: str)</code><a class="headerlink" href="#_create_cousin_filesite_dir-str-rel_path-str-frontmatter-dict-html_content-str" title="Permanent link">¶</a></h3>
<p>Creates a cousin Markdown file with frontmatter and HTML content.</p>
<p><strong>Parameters:</strong>
- <code>site_dir</code> - The MkDocs site output directory
- <code>rel_path</code> - Relative path of the source file
- <code>frontmatter</code> - Dictionary of frontmatter data
- <code>html_content</code> - Extracted HTML content</p>
<h2 id="data-storage">Data Storage<a class="headerlink" href="#data-storage" title="Permanent link">¶</a></h2>
<p>The plugin stores page information during build:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="bp">self</span><span class="o">.</span><span class="n">page_sources</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{</span>
<a href="#__codelineno-2-2" id="__codelineno-2-2" name="__codelineno-2-2"></a>    <span class="s1">'index.md'</span><span class="p">:</span> <span class="p">{</span>
<a href="#__codelineno-2-3" id="__codelineno-2-3" name="__codelineno-2-3"></a>        <span class="s1">'source_path'</span><span class="p">:</span> <span class="s1">'docs/index.md'</span><span class="p">,</span>
<a href="#__codelineno-2-4" id="__codelineno-2-4" name="__codelineno-2-4"></a>        <span class="s1">'frontmatter'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'title'</span><span class="p">:</span> <span class="s1">'Home'</span><span class="p">,</span> <span class="s1">'date'</span><span class="p">:</span> <span class="s1">'2024-01-20'</span><span class="p">}</span>
<a href="#__codelineno-2-5" id="__codelineno-2-5" name="__codelineno-2-5"></a>    <span class="p">},</span>
<a href="#__codelineno-2-6" id="__codelineno-2-6" name="__codelineno-2-6"></a>    <span class="s1">'guide.md'</span><span class="p">:</span> <span class="p">{</span>
<a href="#__codelineno-2-7" id="__codelineno-2-7" name="__codelineno-2-7"></a>        <span class="s1">'source_path'</span><span class="p">:</span> <span class="s1">'docs/guide.md'</span><span class="p">,</span> 
<a href="#__codelineno-2-8" id="__codelineno-2-8" name="__codelineno-2-8"></a>        <span class="s1">'frontmatter'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'title'</span><span class="p">:</span> <span class="s1">'User Guide'</span><span class="p">}</span>
<a href="#__codelineno-2-9" id="__codelineno-2-9" name="__codelineno-2-9"></a>    <span class="p">}</span>
<a href="#__codelineno-2-10" id="__codelineno-2-10" name="__codelineno-2-10"></a><span class="p">}</span>
</code></pre></div>
<h2 id="error-handling">Error Handling<a class="headerlink" href="#error-handling" title="Permanent link">¶</a></h2>
<p>The plugin handles various error cases:</p>
<h3 id="missing-html-element">Missing HTML Element<a class="headerlink" href="#missing-html-element" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="k">if</span> <span class="ow">not</span> <span class="n">element</span><span class="p">:</span>
<a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a>    <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Element '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s1">'html_element'</span><span class="p">]</span><span class="si">}</span><span class="s2">' not found"</span><span class="p">)</span>
<a href="#__codelineno-3-3" id="__codelineno-3-3" name="__codelineno-3-3"></a>    <span class="k">return</span>
</code></pre></div>
<h3 id="invalid-frontmatter">Invalid Frontmatter<a class="headerlink" href="#invalid-frontmatter" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a><span class="k">try</span><span class="p">:</span>
<a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a>    <span class="n">frontmatter</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">fm_text</span><span class="p">)</span> <span class="ow">or</span> <span class="p">{}</span>
<a href="#__codelineno-4-3" id="__codelineno-4-3" name="__codelineno-4-3"></a><span class="k">except</span> <span class="n">yaml</span><span class="o">.</span><span class="n">YAMLError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a href="#__codelineno-4-4" id="__codelineno-4-4" name="__codelineno-4-4"></a>    <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid YAML frontmatter: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<a href="#__codelineno-4-5" id="__codelineno-4-5" name="__codelineno-4-5"></a>    <span class="n">frontmatter</span> <span class="o">=</span> <span class="p">{}</span>
</code></pre></div>
<h3 id="file-io-errors">File I/O Errors<a class="headerlink" href="#file-io-errors" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a><span class="k">try</span><span class="p">:</span>
<a href="#__codelineno-5-2" id="__codelineno-5-2" name="__codelineno-5-2"></a>    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">output_path</span><span class="p">,</span> <span class="s1">'w'</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s1">'utf-8'</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
<a href="#__codelineno-5-3" id="__codelineno-5-3" name="__codelineno-5-3"></a>        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
<a href="#__codelineno-5-4" id="__codelineno-5-4" name="__codelineno-5-4"></a><span class="k">except</span> <span class="ne">IOError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a href="#__codelineno-5-5" id="__codelineno-5-5" name="__codelineno-5-5"></a>    <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to write file: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div>
<h2 id="usage-in-python">Usage in Python<a class="headerlink" href="#usage-in-python" title="Permanent link">¶</a></h2>
<h3 id="programmatic-usage">Programmatic Usage<a class="headerlink" href="#programmatic-usage" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">mkdocs_output_as_input</span><span class="w"> </span><span class="kn">import</span> <span class="n">OutputAsInputPlugin</span>
<a href="#__codelineno-6-2" id="__codelineno-6-2" name="__codelineno-6-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">mkdocs.config</span><span class="w"> </span><span class="kn">import</span> <span class="n">load_config</span>
<a href="#__codelineno-6-3" id="__codelineno-6-3" name="__codelineno-6-3"></a>
<a href="#__codelineno-6-4" id="__codelineno-6-4" name="__codelineno-6-4"></a><span class="c1"># Load MkDocs configuration</span>
<a href="#__codelineno-6-5" id="__codelineno-6-5" name="__codelineno-6-5"></a><span class="n">config</span> <span class="o">=</span> <span class="n">load_config</span><span class="p">(</span><span class="s1">'mkdocs.yml'</span><span class="p">)</span>
<a href="#__codelineno-6-6" id="__codelineno-6-6" name="__codelineno-6-6"></a>
<a href="#__codelineno-6-7" id="__codelineno-6-7" name="__codelineno-6-7"></a><span class="c1"># Create plugin instance</span>
<a href="#__codelineno-6-8" id="__codelineno-6-8" name="__codelineno-6-8"></a><span class="n">plugin</span> <span class="o">=</span> <span class="n">OutputAsInputPlugin</span><span class="p">()</span>
<a href="#__codelineno-6-9" id="__codelineno-6-9" name="__codelineno-6-9"></a><span class="n">plugin</span><span class="o">.</span><span class="n">load_config</span><span class="p">(</span>
<a href="#__codelineno-6-10" id="__codelineno-6-10" name="__codelineno-6-10"></a>    <span class="n">options</span><span class="o">=</span><span class="p">{</span><span class="s1">'stage_dir'</span><span class="p">:</span> <span class="s1">'output'</span><span class="p">,</span> <span class="s1">'verbose'</span><span class="p">:</span> <span class="kc">True</span><span class="p">},</span>
<a href="#__codelineno-6-11" id="__codelineno-6-11" name="__codelineno-6-11"></a>    <span class="n">config_file_path</span><span class="o">=</span><span class="s1">'mkdocs.yml'</span>
<a href="#__codelineno-6-12" id="__codelineno-6-12" name="__codelineno-6-12"></a><span class="p">)</span>
<a href="#__codelineno-6-13" id="__codelineno-6-13" name="__codelineno-6-13"></a>
<a href="#__codelineno-6-14" id="__codelineno-6-14" name="__codelineno-6-14"></a><span class="c1"># Use in custom build process</span>
<a href="#__codelineno-6-15" id="__codelineno-6-15" name="__codelineno-6-15"></a><span class="n">plugin</span><span class="o">.</span><span class="n">on_page_read_source</span><span class="p">(</span><span class="n">page</span><span class="p">,</span> <span class="n">config</span><span class="p">)</span>
<a href="#__codelineno-6-16" id="__codelineno-6-16" name="__codelineno-6-16"></a><span class="n">plugin</span><span class="o">.</span><span class="n">on_post_build</span><span class="p">(</span><span class="n">config</span><span class="p">)</span>
</code></pre></div>
<h3 id="custom-integration">Custom Integration<a class="headerlink" href="#custom-integration" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-7-1" id="__codelineno-7-1" name="__codelineno-7-1"></a><span class="kn">import</span><span class="w"> </span><span class="nn">mkdocs.plugins</span>
<a href="#__codelineno-7-2" id="__codelineno-7-2" name="__codelineno-7-2"></a>
<a href="#__codelineno-7-3" id="__codelineno-7-3" name="__codelineno-7-3"></a><span class="c1"># Register custom event handler</span>
<a href="#__codelineno-7-4" id="__codelineno-7-4" name="__codelineno-7-4"></a><span class="nd">@mkdocs</span><span class="o">.</span><span class="n">plugins</span><span class="o">.</span><span class="n">event_priority</span><span class="p">(</span><span class="mi">50</span><span class="p">)</span>
<a href="#__codelineno-7-5" id="__codelineno-7-5" name="__codelineno-7-5"></a><span class="k">def</span><span class="w"> </span><span class="nf">on_post_build</span><span class="p">(</span><span class="n">config</span><span class="p">):</span>
<a href="#__codelineno-7-6" id="__codelineno-7-6" name="__codelineno-7-6"></a>    <span class="c1"># Custom post-processing after Output as Input</span>
<a href="#__codelineno-7-7" id="__codelineno-7-7" name="__codelineno-7-7"></a>    <span class="n">stage_dir</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">config</span><span class="p">[</span><span class="s1">'plugins'</span><span class="p">][</span><span class="s1">'output-as-input'</span><span class="p">][</span><span class="s1">'stage_dir'</span><span class="p">])</span>
<a href="#__codelineno-7-8" id="__codelineno-7-8" name="__codelineno-7-8"></a>    <span class="k">for</span> <span class="n">md_file</span> <span class="ow">in</span> <span class="n">stage_dir</span><span class="o">.</span><span class="n">glob</span><span class="p">(</span><span class="s1">'**/*.md'</span><span class="p">):</span>
<a href="#__codelineno-7-9" id="__codelineno-7-9" name="__codelineno-7-9"></a>        <span class="c1"># Additional processing</span>
<a href="#__codelineno-7-10" id="__codelineno-7-10" name="__codelineno-7-10"></a>        <span class="n">process_cousin_file</span><span class="p">(</span><span class="n">md_file</span><span class="p">)</span>
</code></pre></div>
<h2 id="cli-tool">CLI Tool<a class="headerlink" href="#cli-tool" title="Permanent link">¶</a></h2>
<p>The plugin includes a CLI tool for testing:</p>
<div class="doc doc-object doc-module">
<a id="mkdocs_output_as_input.cli"></a>
<div class="doc doc-contents first">
<p>CLI tool for standalone processing of HTML files with output-as-input plugin.</p>
<div class="doc doc-children">
<div class="doc doc-object doc-function">
<h2 class="doc doc-heading" id="mkdocs_output_as_input.cli.main">
<code class="highlight language-python"><span class="n">main</span><span class="p">()</span></code>
<a class="headerlink" href="#mkdocs_output_as_input.cli.main" title="Permanent link">¶</a></h2>
<div class="doc doc-contents">
<p>Main CLI entry point.</p>
<details class="quote">
<summary>Source code in <code>src/mkdocs_output_as_input/cli.py</code></summary>
<div class="highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-228">228</a></span>
<span class="normal"><a href="#__codelineno-0-229">229</a></span>
<span class="normal"><a href="#__codelineno-0-230">230</a></span>
<span class="normal"><a href="#__codelineno-0-231">231</a></span>
<span class="normal"><a href="#__codelineno-0-232">232</a></span>
<span class="normal"><a href="#__codelineno-0-233">233</a></span>
<span class="normal"><a href="#__codelineno-0-234">234</a></span>
<span class="normal"><a href="#__codelineno-0-235">235</a></span>
<span class="normal"><a href="#__codelineno-0-236">236</a></span>
<span class="normal"><a href="#__codelineno-0-237">237</a></span>
<span class="normal"><a href="#__codelineno-0-238">238</a></span>
<span class="normal"><a href="#__codelineno-0-239">239</a></span>
<span class="normal"><a href="#__codelineno-0-240">240</a></span>
<span class="normal"><a href="#__codelineno-0-241">241</a></span>
<span class="normal"><a href="#__codelineno-0-242">242</a></span>
<span class="normal"><a href="#__codelineno-0-243">243</a></span>
<span class="normal"><a href="#__codelineno-0-244">244</a></span>
<span class="normal"><a href="#__codelineno-0-245">245</a></span>
<span class="normal"><a href="#__codelineno-0-246">246</a></span>
<span class="normal"><a href="#__codelineno-0-247">247</a></span>
<span class="normal"><a href="#__codelineno-0-248">248</a></span>
<span class="normal"><a href="#__codelineno-0-249">249</a></span>
<span class="normal"><a href="#__codelineno-0-250">250</a></span>
<span class="normal"><a href="#__codelineno-0-251">251</a></span>
<span class="normal"><a href="#__codelineno-0-252">252</a></span>
<span class="normal"><a href="#__codelineno-0-253">253</a></span>
<span class="normal"><a href="#__codelineno-0-254">254</a></span>
<span class="normal"><a href="#__codelineno-0-255">255</a></span>
<span class="normal"><a href="#__codelineno-0-256">256</a></span>
<span class="normal"><a href="#__codelineno-0-257">257</a></span>
<span class="normal"><a href="#__codelineno-0-258">258</a></span>
<span class="normal"><a href="#__codelineno-0-259">259</a></span>
<span class="normal"><a href="#__codelineno-0-260">260</a></span>
<span class="normal"><a href="#__codelineno-0-261">261</a></span>
<span class="normal"><a href="#__codelineno-0-262">262</a></span>
<span class="normal"><a href="#__codelineno-0-263">263</a></span>
<span class="normal"><a href="#__codelineno-0-264">264</a></span>
<span class="normal"><a href="#__codelineno-0-265">265</a></span>
<span class="normal"><a href="#__codelineno-0-266">266</a></span>
<span class="normal"><a href="#__codelineno-0-267">267</a></span>
<span class="normal"><a href="#__codelineno-0-268">268</a></span>
<span class="normal"><a href="#__codelineno-0-269">269</a></span>
<span class="normal"><a href="#__codelineno-0-270">270</a></span>
<span class="normal"><a href="#__codelineno-0-271">271</a></span>
<span class="normal"><a href="#__codelineno-0-272">272</a></span>
<span class="normal"><a href="#__codelineno-0-273">273</a></span>
<span class="normal"><a href="#__codelineno-0-274">274</a></span>
<span class="normal"><a href="#__codelineno-0-275">275</a></span>
<span class="normal"><a href="#__codelineno-0-276">276</a></span>
<span class="normal"><a href="#__codelineno-0-277">277</a></span>
<span class="normal"><a href="#__codelineno-0-278">278</a></span>
<span class="normal"><a href="#__codelineno-0-279">279</a></span>
<span class="normal"><a href="#__codelineno-0-280">280</a></span>
<span class="normal"><a href="#__codelineno-0-281">281</a></span>
<span class="normal"><a href="#__codelineno-0-282">282</a></span>
<span class="normal"><a href="#__codelineno-0-283">283</a></span>
<span class="normal"><a href="#__codelineno-0-284">284</a></span>
<span class="normal"><a href="#__codelineno-0-285">285</a></span>
<span class="normal"><a href="#__codelineno-0-286">286</a></span>
<span class="normal"><a href="#__codelineno-0-287">287</a></span>
<span class="normal"><a href="#__codelineno-0-288">288</a></span>
<span class="normal"><a href="#__codelineno-0-289">289</a></span>
<span class="normal"><a href="#__codelineno-0-290">290</a></span>
<span class="normal"><a href="#__codelineno-0-291">291</a></span>
<span class="normal"><a href="#__codelineno-0-292">292</a></span>
<span class="normal"><a href="#__codelineno-0-293">293</a></span>
<span class="normal"><a href="#__codelineno-0-294">294</a></span>
<span class="normal"><a href="#__codelineno-0-295">295</a></span>
<span class="normal"><a href="#__codelineno-0-296">296</a></span>
<span class="normal"><a href="#__codelineno-0-297">297</a></span>
<span class="normal"><a href="#__codelineno-0-298">298</a></span>
<span class="normal"><a href="#__codelineno-0-299">299</a></span>
<span class="normal"><a href="#__codelineno-0-300">300</a></span>
<span class="normal"><a href="#__codelineno-0-301">301</a></span>
<span class="normal"><a href="#__codelineno-0-302">302</a></span>
<span class="normal"><a href="#__codelineno-0-303">303</a></span>
<span class="normal"><a href="#__codelineno-0-304">304</a></span>
<span class="normal"><a href="#__codelineno-0-305">305</a></span>
<span class="normal"><a href="#__codelineno-0-306">306</a></span>
<span class="normal"><a href="#__codelineno-0-307">307</a></span>
<span class="normal"><a href="#__codelineno-0-308">308</a></span>
<span class="normal"><a href="#__codelineno-0-309">309</a></span>
<span class="normal"><a href="#__codelineno-0-310">310</a></span>
<span class="normal"><a href="#__codelineno-0-311">311</a></span>
<span class="normal"><a href="#__codelineno-0-312">312</a></span>
<span class="normal"><a href="#__codelineno-0-313">313</a></span>
<span class="normal"><a href="#__codelineno-0-314">314</a></span>
<span class="normal"><a href="#__codelineno-0-315">315</a></span>
<span class="normal"><a href="#__codelineno-0-316">316</a></span>
<span class="normal"><a href="#__codelineno-0-317">317</a></span>
<span class="normal"><a href="#__codelineno-0-318">318</a></span>
<span class="normal"><a href="#__codelineno-0-319">319</a></span>
<span class="normal"><a href="#__codelineno-0-320">320</a></span>
<span class="normal"><a href="#__codelineno-0-321">321</a></span>
<span class="normal"><a href="#__codelineno-0-322">322</a></span>
<span class="normal"><a href="#__codelineno-0-323">323</a></span>
<span class="normal"><a href="#__codelineno-0-324">324</a></span>
<span class="normal"><a href="#__codelineno-0-325">325</a></span>
<span class="normal"><a href="#__codelineno-0-326">326</a></span>
<span class="normal"><a href="#__codelineno-0-327">327</a></span>
<span class="normal"><a href="#__codelineno-0-328">328</a></span>
<span class="normal"><a href="#__codelineno-0-329">329</a></span>
<span class="normal"><a href="#__codelineno-0-330">330</a></span>
<span class="normal"><a href="#__codelineno-0-331">331</a></span>
<span class="normal"><a href="#__codelineno-0-332">332</a></span>
<span class="normal"><a href="#__codelineno-0-333">333</a></span>
<span class="normal"><a href="#__codelineno-0-334">334</a></span>
<span class="normal"><a href="#__codelineno-0-335">335</a></span></pre></div></td><td class="code"><div><pre><span></span><code><a id="__codelineno-0-228" name="__codelineno-0-228"></a><span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
<a id="__codelineno-0-229" name="__codelineno-0-229"></a><span class="w">    </span><span class="sd">"""Main CLI entry point."""</span>
<a id="__codelineno-0-230" name="__codelineno-0-230"></a>    <span class="kn">from</span><span class="w"> </span><span class="nn">mkdocs_output_as_input</span><span class="w"> </span><span class="kn">import</span> <span class="n">__version__</span>
<a id="__codelineno-0-231" name="__codelineno-0-231"></a>
<a id="__codelineno-0-232" name="__codelineno-0-232"></a>    <span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">(</span>
<a id="__codelineno-0-233" name="__codelineno-0-233"></a>        <span class="n">description</span><span class="o">=</span><span class="s2">"Process HTML files with MkDocs Output as Input plugin logic"</span><span class="p">,</span>
<a id="__codelineno-0-234" name="__codelineno-0-234"></a>        <span class="n">formatter_class</span><span class="o">=</span><span class="n">argparse</span><span class="o">.</span><span class="n">RawDescriptionHelpFormatter</span><span class="p">,</span>
<a id="__codelineno-0-235" name="__codelineno-0-235"></a>        <span class="n">epilog</span><span class="o">=</span><span class="s2">"""</span>
<a id="__codelineno-0-236" name="__codelineno-0-236"></a><span class="s2">Examples:</span>
<a id="__codelineno-0-237" name="__codelineno-0-237"></a><span class="s2">  # Process a single file</span>
<a id="__codelineno-0-238" name="__codelineno-0-238"></a><span class="s2">  mkdocs-output-as-input process input.html output.md</span>
<a id="__codelineno-0-239" name="__codelineno-0-239"></a>
<a id="__codelineno-0-240" name="__codelineno-0-240"></a><span class="s2">  # Process with custom element and tag</span>
<a id="__codelineno-0-241" name="__codelineno-0-241"></a><span class="s2">  mkdocs-output-as-input process input.html output.md --html-element div --target-tag section</span>
<a id="__codelineno-0-242" name="__codelineno-0-242"></a>
<a id="__codelineno-0-243" name="__codelineno-0-243"></a><span class="s2">  # Process without frontmatter</span>
<a id="__codelineno-0-244" name="__codelineno-0-244"></a><span class="s2">  mkdocs-output-as-input process input.html output.md --no-frontmatter</span>
<a id="__codelineno-0-245" name="__codelineno-0-245"></a>
<a id="__codelineno-0-246" name="__codelineno-0-246"></a><span class="s2">  # Process with link preservation and prettify</span>
<a id="__codelineno-0-247" name="__codelineno-0-247"></a><span class="s2">  mkdocs-output-as-input process input.html output.md --preserve-links --prettify</span>
<a id="__codelineno-0-248" name="__codelineno-0-248"></a><span class="s2">        """</span><span class="p">,</span>
<a id="__codelineno-0-249" name="__codelineno-0-249"></a>    <span class="p">)</span>
<a id="__codelineno-0-250" name="__codelineno-0-250"></a>
<a id="__codelineno-0-251" name="__codelineno-0-251"></a>    <span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span>
<a id="__codelineno-0-252" name="__codelineno-0-252"></a>        <span class="s2">"--version"</span><span class="p">,</span>
<a id="__codelineno-0-253" name="__codelineno-0-253"></a>        <span class="n">action</span><span class="o">=</span><span class="s2">"version"</span><span class="p">,</span>
<a id="__codelineno-0-254" name="__codelineno-0-254"></a>        <span class="n">version</span><span class="o">=</span><span class="sa">f</span><span class="s2">"mkdocs-output-as-input </span><span class="si">{</span><span class="n">__version__</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
<a id="__codelineno-0-255" name="__codelineno-0-255"></a>        <span class="n">help</span><span class="o">=</span><span class="s2">"Show version information and exit"</span><span class="p">,</span>
<a id="__codelineno-0-256" name="__codelineno-0-256"></a>    <span class="p">)</span>
<a id="__codelineno-0-257" name="__codelineno-0-257"></a>
<a id="__codelineno-0-258" name="__codelineno-0-258"></a>    <span class="n">subparsers</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">add_subparsers</span><span class="p">(</span><span class="n">dest</span><span class="o">=</span><span class="s2">"command"</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">"Available commands"</span><span class="p">)</span>
<a id="__codelineno-0-259" name="__codelineno-0-259"></a>
<a id="__codelineno-0-260" name="__codelineno-0-260"></a>    <span class="c1"># Process command</span>
<a id="__codelineno-0-261" name="__codelineno-0-261"></a>    <span class="n">process_parser</span> <span class="o">=</span> <span class="n">subparsers</span><span class="o">.</span><span class="n">add_parser</span><span class="p">(</span><span class="s2">"process"</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">"Process HTML file(s)"</span><span class="p">)</span>
<a id="__codelineno-0-262" name="__codelineno-0-262"></a>    <span class="n">process_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">"input"</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="n">Path</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">"Input HTML file"</span><span class="p">)</span>
<a id="__codelineno-0-263" name="__codelineno-0-263"></a>    <span class="n">process_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">"output"</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="n">Path</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">"Output Markdown file"</span><span class="p">)</span>
<a id="__codelineno-0-264" name="__codelineno-0-264"></a>    <span class="n">process_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span>
<a id="__codelineno-0-265" name="__codelineno-0-265"></a>        <span class="s2">"--html-element"</span><span class="p">,</span>
<a id="__codelineno-0-266" name="__codelineno-0-266"></a>        <span class="n">action</span><span class="o">=</span><span class="s2">"append"</span><span class="p">,</span>
<a id="__codelineno-0-267" name="__codelineno-0-267"></a>        <span class="n">help</span><span class="o">=</span><span class="s2">"HTML element(s) to extract (can be specified multiple times, default: main)"</span><span class="p">,</span>
<a id="__codelineno-0-268" name="__codelineno-0-268"></a>    <span class="p">)</span>
<a id="__codelineno-0-269" name="__codelineno-0-269"></a>    <span class="n">process_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span>
<a id="__codelineno-0-270" name="__codelineno-0-270"></a>        <span class="s2">"--target-tag"</span><span class="p">,</span>
<a id="__codelineno-0-271" name="__codelineno-0-271"></a>        <span class="n">default</span><span class="o">=</span><span class="s2">"article"</span><span class="p">,</span>
<a id="__codelineno-0-272" name="__codelineno-0-272"></a>        <span class="n">help</span><span class="o">=</span><span class="s2">"Target tag for output (default: article)"</span><span class="p">,</span>
<a id="__codelineno-0-273" name="__codelineno-0-273"></a>    <span class="p">)</span>
<a id="__codelineno-0-274" name="__codelineno-0-274"></a>    <span class="n">process_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span>
<a id="__codelineno-0-275" name="__codelineno-0-275"></a>        <span class="s2">"--no-frontmatter"</span><span class="p">,</span>
<a id="__codelineno-0-276" name="__codelineno-0-276"></a>        <span class="n">action</span><span class="o">=</span><span class="s2">"store_false"</span><span class="p">,</span>
<a id="__codelineno-0-277" name="__codelineno-0-277"></a>        <span class="n">dest</span><span class="o">=</span><span class="s2">"include_frontmatter"</span><span class="p">,</span>
<a id="__codelineno-0-278" name="__codelineno-0-278"></a>        <span class="n">help</span><span class="o">=</span><span class="s2">"Exclude frontmatter from output"</span><span class="p">,</span>
<a id="__codelineno-0-279" name="__codelineno-0-279"></a>    <span class="p">)</span>
<a id="__codelineno-0-280" name="__codelineno-0-280"></a>    <span class="n">process_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span>
<a id="__codelineno-0-281" name="__codelineno-0-281"></a>        <span class="s2">"--preserve-links"</span><span class="p">,</span>
<a id="__codelineno-0-282" name="__codelineno-0-282"></a>        <span class="n">action</span><span class="o">=</span><span class="s2">"store_true"</span><span class="p">,</span>
<a id="__codelineno-0-283" name="__codelineno-0-283"></a>        <span class="n">help</span><span class="o">=</span><span class="s2">"Preserve relative links in HTML"</span><span class="p">,</span>
<a id="__codelineno-0-284" name="__codelineno-0-284"></a>    <span class="p">)</span>
<a id="__codelineno-0-285" name="__codelineno-0-285"></a>    <span class="n">process_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span>
<a id="__codelineno-0-286" name="__codelineno-0-286"></a>        <span class="s2">"--minify"</span><span class="p">,</span>
<a id="__codelineno-0-287" name="__codelineno-0-287"></a>        <span class="n">action</span><span class="o">=</span><span class="s2">"store_true"</span><span class="p">,</span>
<a id="__codelineno-0-288" name="__codelineno-0-288"></a>        <span class="n">help</span><span class="o">=</span><span class="s2">"Minify HTML output"</span><span class="p">,</span>
<a id="__codelineno-0-289" name="__codelineno-0-289"></a>    <span class="p">)</span>
<a id="__codelineno-0-290" name="__codelineno-0-290"></a>    <span class="n">process_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span>
<a id="__codelineno-0-291" name="__codelineno-0-291"></a>        <span class="s2">"--prettify"</span><span class="p">,</span>
<a id="__codelineno-0-292" name="__codelineno-0-292"></a>        <span class="n">action</span><span class="o">=</span><span class="s2">"store_true"</span><span class="p">,</span>
<a id="__codelineno-0-293" name="__codelineno-0-293"></a>        <span class="n">help</span><span class="o">=</span><span class="s2">"Prettify HTML output"</span><span class="p">,</span>
<a id="__codelineno-0-294" name="__codelineno-0-294"></a>    <span class="p">)</span>
<a id="__codelineno-0-295" name="__codelineno-0-295"></a>    <span class="n">process_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span>
<a id="__codelineno-0-296" name="__codelineno-0-296"></a>        <span class="s2">"-v"</span><span class="p">,</span> <span class="s2">"--verbose"</span><span class="p">,</span>
<a id="__codelineno-0-297" name="__codelineno-0-297"></a>        <span class="n">action</span><span class="o">=</span><span class="s2">"store_true"</span><span class="p">,</span>
<a id="__codelineno-0-298" name="__codelineno-0-298"></a>        <span class="n">help</span><span class="o">=</span><span class="s2">"Enable verbose logging"</span><span class="p">,</span>
<a id="__codelineno-0-299" name="__codelineno-0-299"></a>    <span class="p">)</span>
<a id="__codelineno-0-300" name="__codelineno-0-300"></a>
<a id="__codelineno-0-301" name="__codelineno-0-301"></a>    <span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<a id="__codelineno-0-302" name="__codelineno-0-302"></a>
<a id="__codelineno-0-303" name="__codelineno-0-303"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">args</span><span class="o">.</span><span class="n">command</span><span class="p">:</span>
<a id="__codelineno-0-304" name="__codelineno-0-304"></a>        <span class="n">parser</span><span class="o">.</span><span class="n">print_help</span><span class="p">()</span>
<a id="__codelineno-0-305" name="__codelineno-0-305"></a>        <span class="k">return</span> <span class="mi">1</span>
<a id="__codelineno-0-306" name="__codelineno-0-306"></a>
<a id="__codelineno-0-307" name="__codelineno-0-307"></a>    <span class="c1"># Set up logging</span>
<a id="__codelineno-0-308" name="__codelineno-0-308"></a>    <span class="n">setup_logging</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">verbose</span><span class="p">)</span>
<a id="__codelineno-0-309" name="__codelineno-0-309"></a>
<a id="__codelineno-0-310" name="__codelineno-0-310"></a>    <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-311" name="__codelineno-0-311"></a>        <span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">command</span> <span class="o">==</span> <span class="s2">"process"</span><span class="p">:</span>
<a id="__codelineno-0-312" name="__codelineno-0-312"></a>            <span class="c1"># Validate mutually exclusive options</span>
<a id="__codelineno-0-313" name="__codelineno-0-313"></a>            <span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">minify</span> <span class="ow">and</span> <span class="n">args</span><span class="o">.</span><span class="n">prettify</span><span class="p">:</span>
<a id="__codelineno-0-314" name="__codelineno-0-314"></a>                <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"Cannot use both --minify and --prettify"</span><span class="p">)</span>
<a id="__codelineno-0-315" name="__codelineno-0-315"></a>                <span class="k">return</span> <span class="mi">1</span>
<a id="__codelineno-0-316" name="__codelineno-0-316"></a>
<a id="__codelineno-0-317" name="__codelineno-0-317"></a>            <span class="c1"># Default to "main" if no elements specified</span>
<a id="__codelineno-0-318" name="__codelineno-0-318"></a>            <span class="n">html_element</span> <span class="o">=</span> <span class="n">args</span><span class="o">.</span><span class="n">html_element</span> <span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">html_element</span> <span class="k">else</span> <span class="s2">"main"</span>
<a id="__codelineno-0-319" name="__codelineno-0-319"></a>
<a id="__codelineno-0-320" name="__codelineno-0-320"></a>            <span class="n">process_file</span><span class="p">(</span>
<a id="__codelineno-0-321" name="__codelineno-0-321"></a>                <span class="n">args</span><span class="o">.</span><span class="n">input</span><span class="p">,</span>
<a id="__codelineno-0-322" name="__codelineno-0-322"></a>                <span class="n">args</span><span class="o">.</span><span class="n">output</span><span class="p">,</span>
<a id="__codelineno-0-323" name="__codelineno-0-323"></a>                <span class="n">html_element</span><span class="o">=</span><span class="n">html_element</span><span class="p">,</span>
<a id="__codelineno-0-324" name="__codelineno-0-324"></a>                <span class="n">target_tag</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">target_tag</span><span class="p">,</span>
<a id="__codelineno-0-325" name="__codelineno-0-325"></a>                <span class="n">include_frontmatter</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">include_frontmatter</span><span class="p">,</span>
<a id="__codelineno-0-326" name="__codelineno-0-326"></a>                <span class="n">preserve_links</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">preserve_links</span><span class="p">,</span>
<a id="__codelineno-0-327" name="__codelineno-0-327"></a>                <span class="n">minify</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">minify</span><span class="p">,</span>
<a id="__codelineno-0-328" name="__codelineno-0-328"></a>                <span class="n">prettify</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">prettify</span><span class="p">,</span>
<a id="__codelineno-0-329" name="__codelineno-0-329"></a>            <span class="p">)</span>
<a id="__codelineno-0-330" name="__codelineno-0-330"></a>            <span class="k">return</span> <span class="mi">0</span>
<a id="__codelineno-0-331" name="__codelineno-0-331"></a>    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-332" name="__codelineno-0-332"></a>        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"Command failed"</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
<a id="__codelineno-0-333" name="__codelineno-0-333"></a>        <span class="k">return</span> <span class="mi">1</span>
<a id="__codelineno-0-334" name="__codelineno-0-334"></a>
<a id="__codelineno-0-335" name="__codelineno-0-335"></a>    <span class="k">return</span> <span class="mi">0</span>
</code></pre></div></td></tr></table></div>
</details>
</div>
</div>
<div class="doc doc-object doc-function">
<h2 class="doc doc-heading" id="mkdocs_output_as_input.cli.process_file">
<code class="highlight language-python"><span class="n">process_file</span><span class="p">(</span><span class="n">input_path</span><span class="p">,</span> <span class="n">output_path</span><span class="p">,</span> <span class="n">html_element</span><span class="o">=</span><span class="s1">'main'</span><span class="p">,</span> <span class="n">target_tag</span><span class="o">=</span><span class="s1">'article'</span><span class="p">,</span> <span class="n">include_frontmatter</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">preserve_links</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">minify</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">prettify</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span></code>
<a class="headerlink" href="#mkdocs_output_as_input.cli.process_file" title="Permanent link">¶</a></h2>
<div class="doc doc-contents">
<p>Process a single file.</p>
<p><span class="doc-section-title">Parameters:</span></p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="doc-section-item">
<td>
<code>input_path</code>
</td>
<td>
<code><span title="pathlib.Path">Path</span></code>
</td>
<td>
<div class="doc-md-description">
<p>Path to input HTML file</p>
</div>
</td>
<td>
<em>required</em>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>output_path</code>
</td>
<td>
<code><span title="pathlib.Path">Path</span></code>
</td>
<td>
<div class="doc-md-description">
<p>Path to output Markdown file</p>
</div>
</td>
<td>
<em>required</em>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>html_element</code>
</td>
<td>
<code><span title="ElementList">ElementList</span></code>
</td>
<td>
<div class="doc-md-description">
<p>CSS selector for element to extract</p>
</div>
</td>
<td>
<code>'main'</code>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>target_tag</code>
</td>
<td>
<code><span title="str">str</span></code>
</td>
<td>
<div class="doc-md-description">
<p>Tag to replace the extracted element with</p>
</div>
</td>
<td>
<code>'article'</code>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>include_frontmatter</code>
</td>
<td>
<code><span title="bool">bool</span></code>
</td>
<td>
<div class="doc-md-description">
<p>Whether to include frontmatter in output</p>
</div>
</td>
<td>
<code>True</code>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>preserve_links</code>
</td>
<td>
<code><span title="bool">bool</span></code>
</td>
<td>
<div class="doc-md-description">
<p>Whether to preserve relative links</p>
</div>
</td>
<td>
<code>False</code>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>minify</code>
</td>
<td>
<code><span title="bool">bool</span></code>
</td>
<td>
<div class="doc-md-description">
<p>Whether to minify the output</p>
</div>
</td>
<td>
<code>False</code>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>prettify</code>
</td>
<td>
<code><span title="bool">bool</span></code>
</td>
<td>
<div class="doc-md-description">
<p>Whether to prettify the output</p>
</div>
</td>
<td>
<code>False</code>
</td>
</tr>
</tbody>
</table>
<details class="quote">
<summary>Source code in <code>src/mkdocs_output_as_input/cli.py</code></summary>
<div class="highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-150">150</a></span>
<span class="normal"><a href="#__codelineno-0-151">151</a></span>
<span class="normal"><a href="#__codelineno-0-152">152</a></span>
<span class="normal"><a href="#__codelineno-0-153">153</a></span>
<span class="normal"><a href="#__codelineno-0-154">154</a></span>
<span class="normal"><a href="#__codelineno-0-155">155</a></span>
<span class="normal"><a href="#__codelineno-0-156">156</a></span>
<span class="normal"><a href="#__codelineno-0-157">157</a></span>
<span class="normal"><a href="#__codelineno-0-158">158</a></span>
<span class="normal"><a href="#__codelineno-0-159">159</a></span>
<span class="normal"><a href="#__codelineno-0-160">160</a></span>
<span class="normal"><a href="#__codelineno-0-161">161</a></span>
<span class="normal"><a href="#__codelineno-0-162">162</a></span>
<span class="normal"><a href="#__codelineno-0-163">163</a></span>
<span class="normal"><a href="#__codelineno-0-164">164</a></span>
<span class="normal"><a href="#__codelineno-0-165">165</a></span>
<span class="normal"><a href="#__codelineno-0-166">166</a></span>
<span class="normal"><a href="#__codelineno-0-167">167</a></span>
<span class="normal"><a href="#__codelineno-0-168">168</a></span>
<span class="normal"><a href="#__codelineno-0-169">169</a></span>
<span class="normal"><a href="#__codelineno-0-170">170</a></span>
<span class="normal"><a href="#__codelineno-0-171">171</a></span>
<span class="normal"><a href="#__codelineno-0-172">172</a></span>
<span class="normal"><a href="#__codelineno-0-173">173</a></span>
<span class="normal"><a href="#__codelineno-0-174">174</a></span>
<span class="normal"><a href="#__codelineno-0-175">175</a></span>
<span class="normal"><a href="#__codelineno-0-176">176</a></span>
<span class="normal"><a href="#__codelineno-0-177">177</a></span>
<span class="normal"><a href="#__codelineno-0-178">178</a></span>
<span class="normal"><a href="#__codelineno-0-179">179</a></span>
<span class="normal"><a href="#__codelineno-0-180">180</a></span>
<span class="normal"><a href="#__codelineno-0-181">181</a></span>
<span class="normal"><a href="#__codelineno-0-182">182</a></span>
<span class="normal"><a href="#__codelineno-0-183">183</a></span>
<span class="normal"><a href="#__codelineno-0-184">184</a></span>
<span class="normal"><a href="#__codelineno-0-185">185</a></span>
<span class="normal"><a href="#__codelineno-0-186">186</a></span>
<span class="normal"><a href="#__codelineno-0-187">187</a></span>
<span class="normal"><a href="#__codelineno-0-188">188</a></span>
<span class="normal"><a href="#__codelineno-0-189">189</a></span>
<span class="normal"><a href="#__codelineno-0-190">190</a></span>
<span class="normal"><a href="#__codelineno-0-191">191</a></span>
<span class="normal"><a href="#__codelineno-0-192">192</a></span>
<span class="normal"><a href="#__codelineno-0-193">193</a></span>
<span class="normal"><a href="#__codelineno-0-194">194</a></span>
<span class="normal"><a href="#__codelineno-0-195">195</a></span>
<span class="normal"><a href="#__codelineno-0-196">196</a></span>
<span class="normal"><a href="#__codelineno-0-197">197</a></span>
<span class="normal"><a href="#__codelineno-0-198">198</a></span>
<span class="normal"><a href="#__codelineno-0-199">199</a></span>
<span class="normal"><a href="#__codelineno-0-200">200</a></span>
<span class="normal"><a href="#__codelineno-0-201">201</a></span>
<span class="normal"><a href="#__codelineno-0-202">202</a></span>
<span class="normal"><a href="#__codelineno-0-203">203</a></span>
<span class="normal"><a href="#__codelineno-0-204">204</a></span>
<span class="normal"><a href="#__codelineno-0-205">205</a></span>
<span class="normal"><a href="#__codelineno-0-206">206</a></span>
<span class="normal"><a href="#__codelineno-0-207">207</a></span>
<span class="normal"><a href="#__codelineno-0-208">208</a></span>
<span class="normal"><a href="#__codelineno-0-209">209</a></span>
<span class="normal"><a href="#__codelineno-0-210">210</a></span>
<span class="normal"><a href="#__codelineno-0-211">211</a></span>
<span class="normal"><a href="#__codelineno-0-212">212</a></span>
<span class="normal"><a href="#__codelineno-0-213">213</a></span>
<span class="normal"><a href="#__codelineno-0-214">214</a></span>
<span class="normal"><a href="#__codelineno-0-215">215</a></span>
<span class="normal"><a href="#__codelineno-0-216">216</a></span>
<span class="normal"><a href="#__codelineno-0-217">217</a></span>
<span class="normal"><a href="#__codelineno-0-218">218</a></span>
<span class="normal"><a href="#__codelineno-0-219">219</a></span>
<span class="normal"><a href="#__codelineno-0-220">220</a></span>
<span class="normal"><a href="#__codelineno-0-221">221</a></span>
<span class="normal"><a href="#__codelineno-0-222">222</a></span>
<span class="normal"><a href="#__codelineno-0-223">223</a></span>
<span class="normal"><a href="#__codelineno-0-224">224</a></span>
<span class="normal"><a href="#__codelineno-0-225">225</a></span></pre></div></td><td class="code"><div><pre><span></span><code><a id="__codelineno-0-150" name="__codelineno-0-150"></a><span class="k">def</span><span class="w"> </span><span class="nf">process_file</span><span class="p">(</span>
<a id="__codelineno-0-151" name="__codelineno-0-151"></a>    <span class="n">input_path</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
<a id="__codelineno-0-152" name="__codelineno-0-152"></a>    <span class="n">output_path</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
<a id="__codelineno-0-153" name="__codelineno-0-153"></a>    <span class="n">html_element</span><span class="p">:</span> <span class="n">ElementList</span> <span class="o">=</span> <span class="s2">"main"</span><span class="p">,</span>
<a id="__codelineno-0-154" name="__codelineno-0-154"></a>    <span class="n">target_tag</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"article"</span><span class="p">,</span>
<a id="__codelineno-0-155" name="__codelineno-0-155"></a>    <span class="n">include_frontmatter</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<a id="__codelineno-0-156" name="__codelineno-0-156"></a>    <span class="n">preserve_links</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<a id="__codelineno-0-157" name="__codelineno-0-157"></a>    <span class="n">minify</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<a id="__codelineno-0-158" name="__codelineno-0-158"></a>    <span class="n">prettify</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<a id="__codelineno-0-159" name="__codelineno-0-159"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<a id="__codelineno-0-160" name="__codelineno-0-160"></a><span class="w">    </span><span class="sd">"""Process a single file.</span>
<a id="__codelineno-0-161" name="__codelineno-0-161"></a>
<a id="__codelineno-0-162" name="__codelineno-0-162"></a><span class="sd">    Args:</span>
<a id="__codelineno-0-163" name="__codelineno-0-163"></a><span class="sd">        input_path: Path to input HTML file</span>
<a id="__codelineno-0-164" name="__codelineno-0-164"></a><span class="sd">        output_path: Path to output Markdown file</span>
<a id="__codelineno-0-165" name="__codelineno-0-165"></a><span class="sd">        html_element: CSS selector for element to extract</span>
<a id="__codelineno-0-166" name="__codelineno-0-166"></a><span class="sd">        target_tag: Tag to replace the extracted element with</span>
<a id="__codelineno-0-167" name="__codelineno-0-167"></a><span class="sd">        include_frontmatter: Whether to include frontmatter in output</span>
<a id="__codelineno-0-168" name="__codelineno-0-168"></a><span class="sd">        preserve_links: Whether to preserve relative links</span>
<a id="__codelineno-0-169" name="__codelineno-0-169"></a><span class="sd">        minify: Whether to minify the output</span>
<a id="__codelineno-0-170" name="__codelineno-0-170"></a><span class="sd">        prettify: Whether to prettify the output</span>
<a id="__codelineno-0-171" name="__codelineno-0-171"></a><span class="sd">    """</span>
<a id="__codelineno-0-172" name="__codelineno-0-172"></a>    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Processing file"</span><span class="p">,</span> <span class="nb">input</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">input_path</span><span class="p">),</span> <span class="n">output</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">output_path</span><span class="p">))</span>
<a id="__codelineno-0-173" name="__codelineno-0-173"></a>
<a id="__codelineno-0-174" name="__codelineno-0-174"></a>    <span class="c1"># Read input file</span>
<a id="__codelineno-0-175" name="__codelineno-0-175"></a>    <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-176" name="__codelineno-0-176"></a>        <span class="n">content</span> <span class="o">=</span> <span class="n">input_path</span><span class="o">.</span><span class="n">read_text</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span>
<a id="__codelineno-0-177" name="__codelineno-0-177"></a>    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-178" name="__codelineno-0-178"></a>        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"Failed to read input file"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">input_path</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
<a id="__codelineno-0-179" name="__codelineno-0-179"></a>        <span class="k">raise</span>
<a id="__codelineno-0-180" name="__codelineno-0-180"></a>
<a id="__codelineno-0-181" name="__codelineno-0-181"></a>    <span class="c1"># Check if there's a corresponding markdown file for frontmatter</span>
<a id="__codelineno-0-182" name="__codelineno-0-182"></a>    <span class="n">frontmatter</span><span class="p">:</span> <span class="n">FrontmatterDict</span> <span class="o">=</span> <span class="p">{}</span>
<a id="__codelineno-0-183" name="__codelineno-0-183"></a>    <span class="k">if</span> <span class="n">include_frontmatter</span><span class="p">:</span>
<a id="__codelineno-0-184" name="__codelineno-0-184"></a>        <span class="n">md_path</span> <span class="o">=</span> <span class="n">input_path</span><span class="o">.</span><span class="n">with_suffix</span><span class="p">(</span><span class="s2">".md"</span><span class="p">)</span>
<a id="__codelineno-0-185" name="__codelineno-0-185"></a>        <span class="k">if</span> <span class="n">md_path</span><span class="o">.</span><span class="n">exists</span><span class="p">():</span>
<a id="__codelineno-0-186" name="__codelineno-0-186"></a>            <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-187" name="__codelineno-0-187"></a>                <span class="n">md_content</span> <span class="o">=</span> <span class="n">md_path</span><span class="o">.</span><span class="n">read_text</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span>
<a id="__codelineno-0-188" name="__codelineno-0-188"></a>                <span class="n">frontmatter</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">extract_frontmatter</span><span class="p">(</span><span class="n">md_content</span><span class="p">)</span>
<a id="__codelineno-0-189" name="__codelineno-0-189"></a>                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Extracted frontmatter"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">md_path</span><span class="p">,</span> <span class="n">keys</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="n">frontmatter</span><span class="o">.</span><span class="n">keys</span><span class="p">()))</span>
<a id="__codelineno-0-190" name="__codelineno-0-190"></a>            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-191" name="__codelineno-0-191"></a>                <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">"Failed to read markdown file"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">md_path</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
<a id="__codelineno-0-192" name="__codelineno-0-192"></a>
<a id="__codelineno-0-193" name="__codelineno-0-193"></a>    <span class="c1"># Process HTML</span>
<a id="__codelineno-0-194" name="__codelineno-0-194"></a>    <span class="n">processed_html</span> <span class="o">=</span> <span class="n">process_html</span><span class="p">(</span>
<a id="__codelineno-0-195" name="__codelineno-0-195"></a>        <span class="n">content</span><span class="p">,</span>
<a id="__codelineno-0-196" name="__codelineno-0-196"></a>        <span class="n">html_element</span><span class="o">=</span><span class="n">html_element</span><span class="p">,</span>
<a id="__codelineno-0-197" name="__codelineno-0-197"></a>        <span class="n">target_tag</span><span class="o">=</span><span class="n">target_tag</span><span class="p">,</span>
<a id="__codelineno-0-198" name="__codelineno-0-198"></a>        <span class="n">preserve_links</span><span class="o">=</span><span class="n">preserve_links</span><span class="p">,</span>
<a id="__codelineno-0-199" name="__codelineno-0-199"></a>        <span class="n">minify</span><span class="o">=</span><span class="n">minify</span><span class="p">,</span>
<a id="__codelineno-0-200" name="__codelineno-0-200"></a>        <span class="n">prettify</span><span class="o">=</span><span class="n">prettify</span><span class="p">,</span>
<a id="__codelineno-0-201" name="__codelineno-0-201"></a>    <span class="p">)</span>
<a id="__codelineno-0-202" name="__codelineno-0-202"></a>
<a id="__codelineno-0-203" name="__codelineno-0-203"></a>    <span class="k">if</span> <span class="n">processed_html</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
<a id="__codelineno-0-204" name="__codelineno-0-204"></a>        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to process HTML from </span><span class="si">{</span><span class="n">input_path</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<a id="__codelineno-0-205" name="__codelineno-0-205"></a>
<a id="__codelineno-0-206" name="__codelineno-0-206"></a>    <span class="c1"># Create output directory if needed</span>
<a id="__codelineno-0-207" name="__codelineno-0-207"></a>    <span class="n">output_path</span><span class="o">.</span><span class="n">parent</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="n">parents</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">exist_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<a id="__codelineno-0-208" name="__codelineno-0-208"></a>
<a id="__codelineno-0-209" name="__codelineno-0-209"></a>    <span class="c1"># Write output</span>
<a id="__codelineno-0-210" name="__codelineno-0-210"></a>    <span class="k">try</span><span class="p">:</span>
<a id="__codelineno-0-211" name="__codelineno-0-211"></a>        <span class="k">with</span> <span class="n">output_path</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">"w"</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
<a id="__codelineno-0-212" name="__codelineno-0-212"></a>            <span class="c1"># Write frontmatter if present and configured</span>
<a id="__codelineno-0-213" name="__codelineno-0-213"></a>            <span class="k">if</span> <span class="n">include_frontmatter</span> <span class="ow">and</span> <span class="n">frontmatter</span><span class="p">:</span>
<a id="__codelineno-0-214" name="__codelineno-0-214"></a>                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">"---</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<a id="__codelineno-0-215" name="__codelineno-0-215"></a>                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">yaml</span><span class="o">.</span><span class="n">safe_dump</span><span class="p">(</span><span class="n">frontmatter</span><span class="p">,</span> <span class="n">default_flow_style</span><span class="o">=</span><span class="kc">False</span><span class="p">))</span>
<a id="__codelineno-0-216" name="__codelineno-0-216"></a>                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">"---</span><span class="se">\n\n</span><span class="s2">"</span><span class="p">)</span>
<a id="__codelineno-0-217" name="__codelineno-0-217"></a>
<a id="__codelineno-0-218" name="__codelineno-0-218"></a>            <span class="c1"># Write processed HTML</span>
<a id="__codelineno-0-219" name="__codelineno-0-219"></a>            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">processed_html</span><span class="p">)</span>
<a id="__codelineno-0-220" name="__codelineno-0-220"></a>            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<a id="__codelineno-0-221" name="__codelineno-0-221"></a>
<a id="__codelineno-0-222" name="__codelineno-0-222"></a>        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Successfully wrote output file"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">output_path</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="n">output_path</span><span class="o">.</span><span class="n">stat</span><span class="p">()</span><span class="o">.</span><span class="n">st_size</span><span class="p">)</span>
<a id="__codelineno-0-223" name="__codelineno-0-223"></a>    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a id="__codelineno-0-224" name="__codelineno-0-224"></a>        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"Failed to write output file"</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">output_path</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
<a id="__codelineno-0-225" name="__codelineno-0-225"></a>        <span class="k">raise</span>
</code></pre></div></td></tr></table></div>
</details>
</div>
</div>
</div>
</div>
</div><h3 id="cli-usage">CLI Usage<a class="headerlink" href="#cli-usage" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-8-1" id="__codelineno-8-1" name="__codelineno-8-1"></a><span class="c1"># Process a single file</span>
<a href="#__codelineno-8-2" id="__codelineno-8-2" name="__codelineno-8-2"></a>output-as-input<span class="w"> </span>process<span class="w"> </span>file.html<span class="w"> </span>--element<span class="w"> </span>main<span class="w"> </span>--output<span class="w"> </span>output.md
<a href="#__codelineno-8-3" id="__codelineno-8-3" name="__codelineno-8-3"></a>
<a href="#__codelineno-8-4" id="__codelineno-8-4" name="__codelineno-8-4"></a><span class="c1"># Process directory</span>
<a href="#__codelineno-8-5" id="__codelineno-8-5" name="__codelineno-8-5"></a>output-as-input<span class="w"> </span>process<span class="w"> </span>site/<span class="w"> </span>--element<span class="w"> </span>article<span class="w"> </span>--stage-dir<span class="w"> </span>stage/
<a href="#__codelineno-8-6" id="__codelineno-8-6" name="__codelineno-8-6"></a>
<a href="#__codelineno-8-7" id="__codelineno-8-7" name="__codelineno-8-7"></a><span class="c1"># With verbose output</span>
<a href="#__codelineno-8-8" id="__codelineno-8-8" name="__codelineno-8-8"></a>output-as-input<span class="w"> </span>process<span class="w"> </span>site/<span class="w"> </span>--verbose
</code></pre></div>
<h2 id="type-hints">Type Hints<a class="headerlink" href="#type-hints" title="Permanent link">¶</a></h2>
<p>The plugin uses type hints for better IDE support:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-9-1" id="__codelineno-9-1" name="__codelineno-9-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Tuple</span>
<a href="#__codelineno-9-2" id="__codelineno-9-2" name="__codelineno-9-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">mkdocs.structure.pages</span><span class="w"> </span><span class="kn">import</span> <span class="n">Page</span>
<a href="#__codelineno-9-3" id="__codelineno-9-3" name="__codelineno-9-3"></a><span class="kn">from</span><span class="w"> </span><span class="nn">mkdocs.config.defaults</span><span class="w"> </span><span class="kn">import</span> <span class="n">MkDocsConfig</span>
<a href="#__codelineno-9-4" id="__codelineno-9-4" name="__codelineno-9-4"></a>
<a href="#__codelineno-9-5" id="__codelineno-9-5" name="__codelineno-9-5"></a><span class="k">def</span><span class="w"> </span><span class="nf">on_page_read_source</span><span class="p">(</span>
<a href="#__codelineno-9-6" id="__codelineno-9-6" name="__codelineno-9-6"></a>    <span class="bp">self</span><span class="p">,</span> 
<a href="#__codelineno-9-7" id="__codelineno-9-7" name="__codelineno-9-7"></a>    <span class="n">page</span><span class="p">:</span> <span class="n">Page</span><span class="p">,</span> 
<a href="#__codelineno-9-8" id="__codelineno-9-8" name="__codelineno-9-8"></a>    <span class="n">config</span><span class="p">:</span> <span class="n">MkDocsConfig</span>
<a href="#__codelineno-9-9" id="__codelineno-9-9" name="__codelineno-9-9"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span> <span class="o">...</span>
<a href="#__codelineno-9-10" id="__codelineno-9-10" name="__codelineno-9-10"></a>
<a href="#__codelineno-9-11" id="__codelineno-9-11" name="__codelineno-9-11"></a><span class="k">def</span><span class="w"> </span><span class="nf">_extract_frontmatter</span><span class="p">(</span>
<a href="#__codelineno-9-12" id="__codelineno-9-12" name="__codelineno-9-12"></a>    <span class="bp">self</span><span class="p">,</span> 
<a href="#__codelineno-9-13" id="__codelineno-9-13" name="__codelineno-9-13"></a>    <span class="n">content</span><span class="p">:</span> <span class="nb">str</span>
<a href="#__codelineno-9-14" id="__codelineno-9-14" name="__codelineno-9-14"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="nb">str</span><span class="p">]:</span> <span class="o">...</span>
</code></pre></div>
<h2 id="logging">Logging<a class="headerlink" href="#logging" title="Permanent link">¶</a></h2>
<p>The plugin uses the <code>loguru</code> logger:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-10-1" id="__codelineno-10-1" name="__codelineno-10-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">loguru</span><span class="w"> </span><span class="kn">import</span> <span class="n">logger</span>
<a href="#__codelineno-10-2" id="__codelineno-10-2" name="__codelineno-10-2"></a>
<a href="#__codelineno-10-3" id="__codelineno-10-3" name="__codelineno-10-3"></a><span class="c1"># Info level (always shown)</span>
<a href="#__codelineno-10-4" id="__codelineno-10-4" name="__codelineno-10-4"></a><span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Processing page: </span><span class="si">{</span><span class="n">page</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">src_path</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<a href="#__codelineno-10-5" id="__codelineno-10-5" name="__codelineno-10-5"></a>
<a href="#__codelineno-10-6" id="__codelineno-10-6" name="__codelineno-10-6"></a><span class="c1"># Debug level (shown with verbose=true)</span>
<a href="#__codelineno-10-7" id="__codelineno-10-7" name="__codelineno-10-7"></a><span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Extracted frontmatter: </span><span class="si">{</span><span class="n">frontmatter</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<a href="#__codelineno-10-8" id="__codelineno-10-8" name="__codelineno-10-8"></a>
<a href="#__codelineno-10-9" id="__codelineno-10-9" name="__codelineno-10-9"></a><span class="c1"># Warning level</span>
<a href="#__codelineno-10-10" id="__codelineno-10-10" name="__codelineno-10-10"></a><span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Element not found: </span><span class="si">{</span><span class="n">element</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<a href="#__codelineno-10-11" id="__codelineno-10-11" name="__codelineno-10-11"></a>
<a href="#__codelineno-10-12" id="__codelineno-10-12" name="__codelineno-10-12"></a><span class="c1"># Error level  </span>
<a href="#__codelineno-10-13" id="__codelineno-10-13" name="__codelineno-10-13"></a><span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to parse HTML: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div>
<h2 id="testing">Testing<a class="headerlink" href="#testing" title="Permanent link">¶</a></h2>
<p>Test helpers for plugin development:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-11-1" id="__codelineno-11-1" name="__codelineno-11-1"></a><span class="kn">import</span><span class="w"> </span><span class="nn">pytest</span>
<a href="#__codelineno-11-2" id="__codelineno-11-2" name="__codelineno-11-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">mkdocs_output_as_input</span><span class="w"> </span><span class="kn">import</span> <span class="n">OutputAsInputPlugin</span>
<a href="#__codelineno-11-3" id="__codelineno-11-3" name="__codelineno-11-3"></a>
<a href="#__codelineno-11-4" id="__codelineno-11-4" name="__codelineno-11-4"></a><span class="nd">@pytest</span><span class="o">.</span><span class="n">fixture</span>
<a href="#__codelineno-11-5" id="__codelineno-11-5" name="__codelineno-11-5"></a><span class="k">def</span><span class="w"> </span><span class="nf">plugin</span><span class="p">():</span>
<a href="#__codelineno-11-6" id="__codelineno-11-6" name="__codelineno-11-6"></a>    <span class="n">plugin</span> <span class="o">=</span> <span class="n">OutputAsInputPlugin</span><span class="p">()</span>
<a href="#__codelineno-11-7" id="__codelineno-11-7" name="__codelineno-11-7"></a>    <span class="n">plugin</span><span class="o">.</span><span class="n">load_config</span><span class="p">(</span><span class="n">options</span><span class="o">=</span><span class="p">{},</span> <span class="n">config_file_path</span><span class="o">=</span><span class="s1">''</span><span class="p">)</span>
<a href="#__codelineno-11-8" id="__codelineno-11-8" name="__codelineno-11-8"></a>    <span class="k">return</span> <span class="n">plugin</span>
<a href="#__codelineno-11-9" id="__codelineno-11-9" name="__codelineno-11-9"></a>
<a href="#__codelineno-11-10" id="__codelineno-11-10" name="__codelineno-11-10"></a><span class="k">def</span><span class="w"> </span><span class="nf">test_frontmatter_extraction</span><span class="p">(</span><span class="n">plugin</span><span class="p">):</span>
<a href="#__codelineno-11-11" id="__codelineno-11-11" name="__codelineno-11-11"></a>    <span class="n">content</span> <span class="o">=</span> <span class="s2">"---</span><span class="se">\n</span><span class="s2">title: Test</span><span class="se">\n</span><span class="s2">---</span><span class="se">\n</span><span class="s2"># Content"</span>
<a href="#__codelineno-11-12" id="__codelineno-11-12" name="__codelineno-11-12"></a>    <span class="n">fm</span><span class="p">,</span> <span class="n">body</span> <span class="o">=</span> <span class="n">plugin</span><span class="o">.</span><span class="n">_extract_frontmatter</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
<a href="#__codelineno-11-13" id="__codelineno-11-13" name="__codelineno-11-13"></a>    <span class="k">assert</span> <span class="n">fm</span> <span class="o">==</span> <span class="p">{</span><span class="s1">'title'</span><span class="p">:</span> <span class="s1">'Test'</span><span class="p">}</span>
<a href="#__codelineno-11-14" id="__codelineno-11-14" name="__codelineno-11-14"></a>    <span class="k">assert</span> <span class="s1">'# Content'</span> <span class="ow">in</span> <span class="n">body</span>
</code></pre></div>
</article>
</div>
<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
</div>
<button class="md-top md-icon" data-md-component="top" hidden="" type="button">
<svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13 20h-2V8l-5.5 5.5-1.42-1.42L12 4.16l7.92 7.92-1.42 1.42L13 8z"></path></svg>
  Back to top
</button>
</article>
