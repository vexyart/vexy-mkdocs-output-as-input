---
description: Quick start guide for the MkDocs Output as Input plugin
title: Getting Started
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
<li class="md-nav__item md-nav__item--active">
<input class="md-nav__toggle md-toggle" id="__toc" type="checkbox"/>
<label class="md-nav__link md-nav__link--active" for="__toc">
<span class="md-ellipsis">
    Getting Started
    
  </span>
<span class="md-nav__icon md-icon"></span>
</label>
<a class="md-nav__link md-nav__link--active" href="./">
<span class="md-ellipsis">
    Getting Started
    
  </span>
</a>
<nav aria-label="Table of contents" class="md-nav md-nav--secondary">
<label class="md-nav__title" for="__toc">
<span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
<ul class="md-nav__list" data-md-component="toc" data-md-scrollfix="">
<li class="md-nav__item">
<a class="md-nav__link" href="#prerequisites">
<span class="md-ellipsis">
      Prerequisites
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#installation">
<span class="md-ellipsis">
      Installation
    </span>
</a>
<nav aria-label="Installation" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#from-pypi">
<span class="md-ellipsis">
      From PyPI
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#from-source">
<span class="md-ellipsis">
      From Source
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#basic-configuration">
<span class="md-ellipsis">
      Basic Configuration
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#your-first-build">
<span class="md-ellipsis">
      Your First Build
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#what-happens-during-build">
<span class="md-ellipsis">
      What Happens During Build?
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#common-use-cases">
<span class="md-ellipsis">
      Common Use Cases
    </span>
</a>
<nav aria-label="Common Use Cases" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#post-processing-with-hugo">
<span class="md-ellipsis">
      Post-Processing with Hugo
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#creating-print-ready-documents">
<span class="md-ellipsis">
      Creating Print-Ready Documents
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#extracting-for-api-documentation">
<span class="md-ellipsis">
      Extracting for API Documentation
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#next-steps">
<span class="md-ellipsis">
      Next Steps
    </span>
</a>
</li>
</ul>
</nav>
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
<a class="md-nav__link" href="#prerequisites">
<span class="md-ellipsis">
      Prerequisites
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#installation">
<span class="md-ellipsis">
      Installation
    </span>
</a>
<nav aria-label="Installation" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#from-pypi">
<span class="md-ellipsis">
      From PyPI
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#from-source">
<span class="md-ellipsis">
      From Source
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#basic-configuration">
<span class="md-ellipsis">
      Basic Configuration
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#your-first-build">
<span class="md-ellipsis">
      Your First Build
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#what-happens-during-build">
<span class="md-ellipsis">
      What Happens During Build?
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#common-use-cases">
<span class="md-ellipsis">
      Common Use Cases
    </span>
</a>
<nav aria-label="Common Use Cases" class="md-nav">
<ul class="md-nav__list">
<li class="md-nav__item">
<a class="md-nav__link" href="#post-processing-with-hugo">
<span class="md-ellipsis">
      Post-Processing with Hugo
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#creating-print-ready-documents">
<span class="md-ellipsis">
      Creating Print-Ready Documents
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#extracting-for-api-documentation">
<span class="md-ellipsis">
      Extracting for API Documentation
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#next-steps">
<span class="md-ellipsis">
      Next Steps
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
<h1 id="getting-started">Getting Started<a class="headerlink" href="#getting-started" title="Permanent link">¶</a></h1>
<p>This guide will help you get up and running with the MkDocs Output as Input plugin in minutes.</p>
<h2 id="prerequisites">Prerequisites<a class="headerlink" href="#prerequisites" title="Permanent link">¶</a></h2>
<ul>
<li>Python 3.8 or higher</li>
<li>MkDocs 1.4.0 or higher</li>
<li>Basic familiarity with MkDocs</li>
</ul>
<h2 id="installation">Installation<a class="headerlink" href="#installation" title="Permanent link">¶</a></h2>
<h3 id="from-pypi">From PyPI<a class="headerlink" href="#from-pypi" title="Permanent link">¶</a></h3>
<p>The easiest way to install the plugin is from PyPI:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a>pip<span class="w"> </span>install<span class="w"> </span>mkdocs-output-as-input
</code></pre></div>
<h3 id="from-source">From Source<a class="headerlink" href="#from-source" title="Permanent link">¶</a></h3>
<p>For development or to get the latest features:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a>git<span class="w"> </span>clone<span class="w"> </span>https://github.com/vexyart/vexy-mkdocs-output-as-input.git
<a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a><span class="nb">cd</span><span class="w"> </span>vexy-mkdocs-output-as-input
<a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a>pip<span class="w"> </span>install<span class="w"> </span>-e<span class="w"> </span>.
</code></pre></div>
<h2 id="basic-configuration">Basic Configuration<a class="headerlink" href="#basic-configuration" title="Permanent link">¶</a></h2>
<p>Add the plugin to your <code>mkdocs.yml</code>:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-2-2" id="__codelineno-2-2" name="__codelineno-2-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">output-as-input</span>
</code></pre></div>
<p>This uses the default configuration:
- Output directory: <code>stage/</code>
- HTML element to extract: <code>&lt;main&gt;</code>
- Wrapper tag: <code>&lt;article&gt;</code></p>
<h2 id="your-first-build">Your First Build<a class="headerlink" href="#your-first-build" title="Permanent link">¶</a></h2>
<ol>
<li>Create a simple MkDocs project:</li>
</ol>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a>mkdocs<span class="w"> </span>new<span class="w"> </span>my-project
<a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a><span class="nb">cd</span><span class="w"> </span>my-project
</code></pre></div>
<ol>
<li>Add some frontmatter to <code>docs/index.md</code>:</li>
</ol>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a>---
<a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a>title: Home
<a href="#__codelineno-4-3" id="__codelineno-4-3" name="__codelineno-4-3"></a>date: 2024-01-20
<a href="#__codelineno-4-4" id="__codelineno-4-4" name="__codelineno-4-4"></a><span class="gu">tags: [intro, welcome]</span>
<a href="#__codelineno-4-5" id="__codelineno-4-5" name="__codelineno-4-5"></a><span class="gu">---</span>
<a href="#__codelineno-4-6" id="__codelineno-4-6" name="__codelineno-4-6"></a>
<a href="#__codelineno-4-7" id="__codelineno-4-7" name="__codelineno-4-7"></a><span class="gh"># Welcome to My Docs</span>
<a href="#__codelineno-4-8" id="__codelineno-4-8" name="__codelineno-4-8"></a>
<a href="#__codelineno-4-9" id="__codelineno-4-9" name="__codelineno-4-9"></a>This is a test page.
</code></pre></div>
<ol>
<li>Configure the plugin in <code>mkdocs.yml</code>:</li>
</ol>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a><span class="nt">site_name</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">My Docs</span>
<a href="#__codelineno-5-2" id="__codelineno-5-2" name="__codelineno-5-2"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-5-3" id="__codelineno-5-3" name="__codelineno-5-3"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-5-4" id="__codelineno-5-4" name="__codelineno-5-4"></a><span class="w">      </span><span class="nt">verbose</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">true</span>
</code></pre></div>
<ol>
<li>Build your site:</li>
</ol>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a>mkdocs<span class="w"> </span>build
</code></pre></div>
<ol>
<li>Check the output in <code>stage/index.md</code>:</li>
</ol>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-7-1" id="__codelineno-7-1" name="__codelineno-7-1"></a>---
<a href="#__codelineno-7-2" id="__codelineno-7-2" name="__codelineno-7-2"></a>title: Home
<a href="#__codelineno-7-3" id="__codelineno-7-3" name="__codelineno-7-3"></a>date: 2024-01-20
<a href="#__codelineno-7-4" id="__codelineno-7-4" name="__codelineno-7-4"></a><span class="gu">tags: [intro, welcome]</span>
<a href="#__codelineno-7-5" id="__codelineno-7-5" name="__codelineno-7-5"></a><span class="gu">---</span>
<a href="#__codelineno-7-6" id="__codelineno-7-6" name="__codelineno-7-6"></a>
<a href="#__codelineno-7-7" id="__codelineno-7-7" name="__codelineno-7-7"></a>&lt;article&gt;
<a href="#__codelineno-7-8" id="__codelineno-7-8" name="__codelineno-7-8"></a>&lt;h1&gt;Welcome to My Docs&lt;/h1&gt;
<a href="#__codelineno-7-9" id="__codelineno-7-9" name="__codelineno-7-9"></a>&lt;p&gt;This is a test page.&lt;/p&gt;
<a href="#__codelineno-7-10" id="__codelineno-7-10" name="__codelineno-7-10"></a>&lt;/article&gt;
</code></pre></div>
<h2 id="what-happens-during-build">What Happens During Build?<a class="headerlink" href="#what-happens-during-build" title="Permanent link">¶</a></h2>
<ol>
<li><strong>Source Reading</strong>: The plugin captures each Markdown file and its frontmatter</li>
<li><strong>HTML Generation</strong>: MkDocs renders your Markdown to HTML as usual</li>
<li><strong>HTML Extraction</strong>: The plugin extracts the specified HTML element from each page</li>
<li><strong>File Creation</strong>: Cousin files are created in the stage directory with:</li>
<li>Original YAML frontmatter</li>
<li>Extracted HTML wrapped in your target tag</li>
</ol>
<h2 id="common-use-cases">Common Use Cases<a class="headerlink" href="#common-use-cases" title="Permanent link">¶</a></h2>
<h3 id="post-processing-with-hugo">Post-Processing with Hugo<a class="headerlink" href="#post-processing-with-hugo" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-8-1" id="__codelineno-8-1" name="__codelineno-8-1"></a><span class="c1"># mkdocs.yml</span>
<a href="#__codelineno-8-2" id="__codelineno-8-2" name="__codelineno-8-2"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-8-3" id="__codelineno-8-3" name="__codelineno-8-3"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-8-4" id="__codelineno-8-4" name="__codelineno-8-4"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">../hugo-site/content</span>
<a href="#__codelineno-8-5" id="__codelineno-8-5" name="__codelineno-8-5"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">div</span>
</code></pre></div>
<h3 id="creating-print-ready-documents">Creating Print-Ready Documents<a class="headerlink" href="#creating-print-ready-documents" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-9-1" id="__codelineno-9-1" name="__codelineno-9-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-9-2" id="__codelineno-9-2" name="__codelineno-9-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-9-3" id="__codelineno-9-3" name="__codelineno-9-3"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">article</span>
<a href="#__codelineno-9-4" id="__codelineno-9-4" name="__codelineno-9-4"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">print-ready</span>
</code></pre></div>
<h3 id="extracting-for-api-documentation">Extracting for API Documentation<a class="headerlink" href="#extracting-for-api-documentation" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-10-1" id="__codelineno-10-1" name="__codelineno-10-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-10-2" id="__codelineno-10-2" name="__codelineno-10-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-10-3" id="__codelineno-10-3" name="__codelineno-10-3"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="s">".api-content"</span>
<a href="#__codelineno-10-4" id="__codelineno-10-4" name="__codelineno-10-4"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">section</span>
</code></pre></div>
<h2 id="next-steps">Next Steps<a class="headerlink" href="#next-steps" title="Permanent link">¶</a></h2>
<ul>
<li>Learn about all <a href="../configuration/">Configuration Options</a></li>
<li>See more <a href="../examples/">Examples</a></li>
<li>Read the <a href="../api/">API Reference</a> for advanced usage</li>
</ul>
</article>
</div>
<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
</div>
<button class="md-top md-icon" data-md-component="top" hidden="" type="button">
<svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13 20h-2V8l-5.5 5.5-1.42-1.42L12 4.16l7.92 7.92-1.42 1.42L13 8z"></path></svg>
  Back to top
</button>
</article>
