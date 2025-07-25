---
description: Complete configuration reference for the MkDocs Output as Input plugin
title: Configuration
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
<li class="md-nav__item md-nav__item--active">
<input class="md-nav__toggle md-toggle" id="__toc" type="checkbox"/>
<label class="md-nav__link md-nav__link--active" for="__toc">
<span class="md-ellipsis">
    Configuration
    
  </span>
<span class="md-nav__icon md-icon"></span>
</label>
<a class="md-nav__link md-nav__link--active" href="./">
<span class="md-ellipsis">
    Configuration
    
  </span>
</a>
<nav aria-label="Table of contents" class="md-nav md-nav--secondary">
<label class="md-nav__title" for="__toc">
<span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
<ul class="md-nav__list" data-md-component="toc" data-md-scrollfix="">
<li class="md-nav__item">
<a class="md-nav__link" href="#configuration-options">
<span class="md-ellipsis">
      Configuration Options
    </span>
</a>
<nav aria-label="Configuration Options" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#stage_dir">
<span class="md-ellipsis">
      stage_dir
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#html_element">
<span class="md-ellipsis">
      html_element
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#target_tag">
<span class="md-ellipsis">
      target_tag
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#verbose">
<span class="md-ellipsis">
      verbose
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#complete-example">
<span class="md-ellipsis">
      Complete Example
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#configuration-patterns">
<span class="md-ellipsis">
      Configuration Patterns
    </span>
</a>
<nav aria-label="Configuration Patterns" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#for-static-site-generators">
<span class="md-ellipsis">
      For Static Site Generators
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#for-different-themes">
<span class="md-ellipsis">
      For Different Themes
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#for-printpdf-generation">
<span class="md-ellipsis">
      For Print/PDF Generation
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#environment-variables">
<span class="md-ellipsis">
      Environment Variables
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#validation">
<span class="md-ellipsis">
      Validation
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#default-behavior">
<span class="md-ellipsis">
      Default Behavior
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="../examples/">
<span class="md-ellipsis">
    Examples
    
  </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="../api/">
<span class="md-ellipsis">
    API Reference
    
  </span>
</a>
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
<a class="md-nav__link" href="#configuration-options">
<span class="md-ellipsis">
      Configuration Options
    </span>
</a>
<nav aria-label="Configuration Options" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#stage_dir">
<span class="md-ellipsis">
      stage_dir
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#html_element">
<span class="md-ellipsis">
      html_element
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#target_tag">
<span class="md-ellipsis">
      target_tag
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#verbose">
<span class="md-ellipsis">
      verbose
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#complete-example">
<span class="md-ellipsis">
      Complete Example
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#configuration-patterns">
<span class="md-ellipsis">
      Configuration Patterns
    </span>
</a>
<nav aria-label="Configuration Patterns" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#for-static-site-generators">
<span class="md-ellipsis">
      For Static Site Generators
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#for-different-themes">
<span class="md-ellipsis">
      For Different Themes
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#for-printpdf-generation">
<span class="md-ellipsis">
      For Print/PDF Generation
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#environment-variables">
<span class="md-ellipsis">
      Environment Variables
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#validation">
<span class="md-ellipsis">
      Validation
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#default-behavior">
<span class="md-ellipsis">
      Default Behavior
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
<h1 id="configuration">Configuration<a class="headerlink" href="#configuration" title="Permanent link">¶</a></h1>
<p>The MkDocs Output as Input plugin provides several configuration options to customize its behavior. All options are set in your <code>mkdocs.yml</code> file.</p>
<h2 id="configuration-options">Configuration Options<a class="headerlink" href="#configuration-options" title="Permanent link">¶</a></h2>
<h3 id="stage_dir"><code>stage_dir</code><a class="headerlink" href="#stage_dir" title="Permanent link">¶</a></h3>
<p><strong>Type</strong>: <code>str</code><br/>
<strong>Default</strong>: <code>"stage"</code></p>
<p>The directory where cousin files will be created. Can be relative to the MkDocs project root or an absolute path.</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="s">"output/markdown"</span>
</code></pre></div>
<div class="admonition tip">
<p class="admonition-title">Tip</p>
<p>Use an absolute path to place files outside your project:
<div class="highlight"><pre><span></span><code><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="s">"/var/www/content"</span>
</code></pre></div></p>
</div>
<h3 id="html_element"><code>html_element</code><a class="headerlink" href="#html_element" title="Permanent link">¶</a></h3>
<p><strong>Type</strong>: <code>str</code><br/>
<strong>Default</strong>: <code>"main"</code></p>
<p>The HTML element or CSS selector to extract from rendered pages. </p>
<p>Common values:
- <code>"main"</code> - Main content area (default)
- <code>"article"</code> - Article content
- <code>"#content"</code> - Element with id="content"
- <code>".documentation"</code> - Elements with class="documentation"
- <code>"div.content"</code> - Div elements with class="content"</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-2-2" id="__codelineno-2-2" name="__codelineno-2-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-2-3" id="__codelineno-2-3" name="__codelineno-2-3"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="s">"article"</span>
</code></pre></div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>If the specified element is not found, the plugin will log a warning and skip that page.</p>
</div>
<h3 id="target_tag"><code>target_tag</code><a class="headerlink" href="#target_tag" title="Permanent link">¶</a></h3>
<p><strong>Type</strong>: <code>str</code><br/>
<strong>Default</strong>: <code>"article"</code></p>
<p>The HTML tag used to wrap the extracted content in cousin files.</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-3-3" id="__codelineno-3-3" name="__codelineno-3-3"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="s">"section"</span>
</code></pre></div>
<p>This would produce:
<div class="highlight"><pre><span></span><code><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a>---
<a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a><span class="gu">title: Page Title</span>
<a href="#__codelineno-4-3" id="__codelineno-4-3" name="__codelineno-4-3"></a><span class="gu">---</span>
<a href="#__codelineno-4-4" id="__codelineno-4-4" name="__codelineno-4-4"></a>
<a href="#__codelineno-4-5" id="__codelineno-4-5" name="__codelineno-4-5"></a>&lt;section&gt;
<a href="#__codelineno-4-6" id="__codelineno-4-6" name="__codelineno-4-6"></a>&lt;!-- extracted content --&gt;
<a href="#__codelineno-4-7" id="__codelineno-4-7" name="__codelineno-4-7"></a>&lt;/section&gt;
</code></pre></div></p>
<h3 id="verbose"><code>verbose</code><a class="headerlink" href="#verbose" title="Permanent link">¶</a></h3>
<p><strong>Type</strong>: <code>bool</code><br/>
<strong>Default</strong>: <code>false</code></p>
<p>Enable detailed debug logging to help troubleshoot issues.</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-5-2" id="__codelineno-5-2" name="__codelineno-5-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-5-3" id="__codelineno-5-3" name="__codelineno-5-3"></a><span class="w">      </span><span class="nt">verbose</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">true</span>
</code></pre></div>
<p>When enabled, the plugin logs:
- Each file being processed
- Extraction results
- Any errors or warnings
- File creation details</p>
<h2 id="complete-example">Complete Example<a class="headerlink" href="#complete-example" title="Permanent link">¶</a></h2>
<p>Here's a complete configuration example showing all options:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a><span class="nt">site_name</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">My Documentation</span>
<a href="#__codelineno-6-2" id="__codelineno-6-2" name="__codelineno-6-2"></a><span class="nt">site_url</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">https://example.com/docs/</span>
<a href="#__codelineno-6-3" id="__codelineno-6-3" name="__codelineno-6-3"></a>
<a href="#__codelineno-6-4" id="__codelineno-6-4" name="__codelineno-6-4"></a><span class="nt">theme</span><span class="p">:</span>
<a href="#__codelineno-6-5" id="__codelineno-6-5" name="__codelineno-6-5"></a><span class="w">  </span><span class="nt">name</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">material</span>
<a href="#__codelineno-6-6" id="__codelineno-6-6" name="__codelineno-6-6"></a>
<a href="#__codelineno-6-7" id="__codelineno-6-7" name="__codelineno-6-7"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-6-8" id="__codelineno-6-8" name="__codelineno-6-8"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">search</span>
<a href="#__codelineno-6-9" id="__codelineno-6-9" name="__codelineno-6-9"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-6-10" id="__codelineno-6-10" name="__codelineno-6-10"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="s">"staged-content"</span>
<a href="#__codelineno-6-11" id="__codelineno-6-11" name="__codelineno-6-11"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="s">"article.md-content"</span>
<a href="#__codelineno-6-12" id="__codelineno-6-12" name="__codelineno-6-12"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="s">"div"</span>
<a href="#__codelineno-6-13" id="__codelineno-6-13" name="__codelineno-6-13"></a><span class="w">      </span><span class="nt">verbose</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">true</span>
<a href="#__codelineno-6-14" id="__codelineno-6-14" name="__codelineno-6-14"></a>
<a href="#__codelineno-6-15" id="__codelineno-6-15" name="__codelineno-6-15"></a><span class="nt">nav</span><span class="p">:</span>
<a href="#__codelineno-6-16" id="__codelineno-6-16" name="__codelineno-6-16"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">Home</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">index.md</span>
<a href="#__codelineno-6-17" id="__codelineno-6-17" name="__codelineno-6-17"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">Guide</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">guide.md</span>
<a href="#__codelineno-6-18" id="__codelineno-6-18" name="__codelineno-6-18"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">API</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">api.md</span>
</code></pre></div>
<h2 id="configuration-patterns">Configuration Patterns<a class="headerlink" href="#configuration-patterns" title="Permanent link">¶</a></h2>
<h3 id="for-static-site-generators">For Static Site Generators<a class="headerlink" href="#for-static-site-generators" title="Permanent link">¶</a></h3>
<p>When using with Hugo:
<div class="highlight"><pre><span></span><code><a href="#__codelineno-7-1" id="__codelineno-7-1" name="__codelineno-7-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-7-2" id="__codelineno-7-2" name="__codelineno-7-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-7-3" id="__codelineno-7-3" name="__codelineno-7-3"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="s">"../hugo/content/docs"</span>
<a href="#__codelineno-7-4" id="__codelineno-7-4" name="__codelineno-7-4"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="s">"main"</span>
<a href="#__codelineno-7-5" id="__codelineno-7-5" name="__codelineno-7-5"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="s">"div"</span><span class="w">  </span><span class="c1"># Hugo prefers div</span>
</code></pre></div></p>
<p>When using with Jekyll:
<div class="highlight"><pre><span></span><code><a href="#__codelineno-8-1" id="__codelineno-8-1" name="__codelineno-8-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-8-2" id="__codelineno-8-2" name="__codelineno-8-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-8-3" id="__codelineno-8-3" name="__codelineno-8-3"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="s">"../jekyll/_posts"</span>
<a href="#__codelineno-8-4" id="__codelineno-8-4" name="__codelineno-8-4"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="s">"article"</span>
<a href="#__codelineno-8-5" id="__codelineno-8-5" name="__codelineno-8-5"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="s">"article"</span>
</code></pre></div></p>
<h3 id="for-different-themes">For Different Themes<a class="headerlink" href="#for-different-themes" title="Permanent link">¶</a></h3>
<p>Material for MkDocs:
<div class="highlight"><pre><span></span><code><a href="#__codelineno-9-1" id="__codelineno-9-1" name="__codelineno-9-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-9-2" id="__codelineno-9-2" name="__codelineno-9-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-9-3" id="__codelineno-9-3" name="__codelineno-9-3"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="s">"article.md-content__inner"</span>
</code></pre></div></p>
<p>ReadTheDocs theme:
<div class="highlight"><pre><span></span><code><a href="#__codelineno-10-1" id="__codelineno-10-1" name="__codelineno-10-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-10-2" id="__codelineno-10-2" name="__codelineno-10-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-10-3" id="__codelineno-10-3" name="__codelineno-10-3"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="s">"div.rst-content"</span>
</code></pre></div></p>
<p>Default MkDocs theme:
<div class="highlight"><pre><span></span><code><a href="#__codelineno-11-1" id="__codelineno-11-1" name="__codelineno-11-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-11-2" id="__codelineno-11-2" name="__codelineno-11-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-11-3" id="__codelineno-11-3" name="__codelineno-11-3"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="s">"div.col-md-9"</span>
</code></pre></div></p>
<h3 id="for-printpdf-generation">For Print/PDF Generation<a class="headerlink" href="#for-printpdf-generation" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-12-1" id="__codelineno-12-1" name="__codelineno-12-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-12-2" id="__codelineno-12-2" name="__codelineno-12-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-12-3" id="__codelineno-12-3" name="__codelineno-12-3"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="s">"print-output"</span>
<a href="#__codelineno-12-4" id="__codelineno-12-4" name="__codelineno-12-4"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="s">"main"</span>
<a href="#__codelineno-12-5" id="__codelineno-12-5" name="__codelineno-12-5"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="s">"div"</span>
<a href="#__codelineno-12-6" id="__codelineno-12-6" name="__codelineno-12-6"></a><span class="w">      </span><span class="c1"># Then use pandoc or similar to convert</span>
</code></pre></div>
<h2 id="environment-variables">Environment Variables<a class="headerlink" href="#environment-variables" title="Permanent link">¶</a></h2>
<p>You can use environment variables in configuration:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-13-1" id="__codelineno-13-1" name="__codelineno-13-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-13-2" id="__codelineno-13-2" name="__codelineno-13-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-13-3" id="__codelineno-13-3" name="__codelineno-13-3"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="s">"${OUTPUT_DIR:-stage}"</span>
<a href="#__codelineno-13-4" id="__codelineno-13-4" name="__codelineno-13-4"></a><span class="w">      </span><span class="nt">verbose</span><span class="p">:</span><span class="w"> </span><span class="s">"${DEBUG:-false}"</span>
</code></pre></div>
<h2 id="validation">Validation<a class="headerlink" href="#validation" title="Permanent link">¶</a></h2>
<p>The plugin validates configuration on startup:</p>
<ul>
<li><code>stage_dir</code> must be a valid path</li>
<li><code>html_element</code> must be a non-empty string</li>
<li><code>target_tag</code> must be a valid HTML tag name</li>
<li><code>verbose</code> must be a boolean</li>
</ul>
<p>Invalid configuration will raise an error during MkDocs build.</p>
<h2 id="default-behavior">Default Behavior<a class="headerlink" href="#default-behavior" title="Permanent link">¶</a></h2>
<p>With no configuration, the plugin uses these defaults:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-14-1" id="__codelineno-14-1" name="__codelineno-14-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-14-2" id="__codelineno-14-2" name="__codelineno-14-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">output-as-input</span>
<a href="#__codelineno-14-3" id="__codelineno-14-3" name="__codelineno-14-3"></a><span class="w">  </span><span class="c1"># Equivalent to:</span>
<a href="#__codelineno-14-4" id="__codelineno-14-4" name="__codelineno-14-4"></a><span class="w">  </span><span class="c1"># - output-as-input:</span>
<a href="#__codelineno-14-5" id="__codelineno-14-5" name="__codelineno-14-5"></a><span class="w">  </span><span class="c1">#     stage_dir: "stage"</span>
<a href="#__codelineno-14-6" id="__codelineno-14-6" name="__codelineno-14-6"></a><span class="w">  </span><span class="c1">#     html_element: "main"</span>
<a href="#__codelineno-14-7" id="__codelineno-14-7" name="__codelineno-14-7"></a><span class="w">  </span><span class="c1">#     target_tag: "article"</span>
<a href="#__codelineno-14-8" id="__codelineno-14-8" name="__codelineno-14-8"></a><span class="w">  </span><span class="c1">#     verbose: false</span>
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
