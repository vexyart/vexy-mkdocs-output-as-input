---
description: A powerful MkDocs plugin that captures rendered HTML output and creates
  cousin Markdown files for post-processing workflows
title: MkDocs Output as Input Plugin
---

<article class="md-main" data-md-component="main">
<div class="md-main__inner md-grid">
<div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation">
<div class="md-sidebar__scrollwrap">
<div class="md-sidebar__inner">
<nav aria-label="Navigation" class="md-nav md-nav--primary" data-md-level="0">
<label class="md-nav__title" for="__drawer">
<a aria-label="MkDocs Output as Input Plugin" class="md-nav__button md-logo" data-md-component="logo" href="." title="MkDocs Output as Input Plugin">
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
<li class="md-nav__item md-nav__item--active">
<input class="md-nav__toggle md-toggle" id="__toc" type="checkbox"/>
<label class="md-nav__link md-nav__link--active" for="__toc">
<span class="md-ellipsis">
    Home
    
  </span>
<span class="md-nav__icon md-icon"></span>
</label>
<a class="md-nav__link md-nav__link--active" href=".">
<span class="md-ellipsis">
    Home
    
  </span>
</a>
<nav aria-label="Table of contents" class="md-nav md-nav--secondary">
<label class="md-nav__title" for="__toc">
<span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
<ul class="md-nav__list" data-md-component="toc" data-md-scrollfix="">
<li class="md-nav__item">
<a class="md-nav__link" href="#what-is-output-as-input">
<span class="md-ellipsis">
      What is Output as Input?
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#key-features">
<span class="md-ellipsis">
      Key Features
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#quick-start">
<span class="md-ellipsis">
      Quick Start
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#next-steps">
<span class="md-ellipsis">
      Next Steps
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#support">
<span class="md-ellipsis">
      Support
    </span>
</a>
</li>
</ul>
</nav>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="getting-started/">
<span class="md-ellipsis">
    Getting Started
    
  </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="configuration/">
<span class="md-ellipsis">
    Configuration
    
  </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="examples/">
<span class="md-ellipsis">
    Examples
    
  </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="api/">
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
<a class="md-nav__link" href="#what-is-output-as-input">
<span class="md-ellipsis">
      What is Output as Input?
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#key-features">
<span class="md-ellipsis">
      Key Features
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#quick-start">
<span class="md-ellipsis">
      Quick Start
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#next-steps">
<span class="md-ellipsis">
      Next Steps
    </span>
</a>
</li>
<li class="md-nav__item">
<a class="md-nav__link" href="#support">
<span class="md-ellipsis">
      Support
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
<h1 id="mkdocs-output-as-input-plugin">MkDocs Output as Input Plugin<a class="headerlink" href="#mkdocs-output-as-input-plugin" title="Permanent link">¶</a></h1>
<p>Welcome to the <strong>MkDocs Output as Input Plugin</strong> documentation! This plugin enables advanced documentation workflows by capturing rendered HTML output from MkDocs and creating "cousin" Markdown files that combine original YAML frontmatter with extracted HTML content.</p>
<h2 id="what-is-output-as-input">What is Output as Input?<a class="headerlink" href="#what-is-output-as-input" title="Permanent link">¶</a></h2>
<p>The Output as Input plugin bridges the gap between MkDocs and other static site generators by:</p>
<ul>
<li>📄 <strong>Capturing rendered HTML</strong> from your MkDocs build</li>
<li>🔄 <strong>Preserving YAML frontmatter</strong> from source Markdown files  </li>
<li>📁 <strong>Creating cousin files</strong> in a staging directory for further processing</li>
<li>🛠️ <strong>Enabling post-processing workflows</strong> with other tools</li>
</ul>
<h2 id="key-features">Key Features<a class="headerlink" href="#key-features" title="Permanent link">¶</a></h2>
<ul>
<li><strong>Flexible HTML extraction</strong> - Target specific HTML elements (main, article, div, etc.)</li>
<li><strong>Frontmatter preservation</strong> - Maintains all YAML metadata from source files</li>
<li><strong>Configurable output</strong> - Customize staging directory and wrapper tags</li>
<li><strong>Error resilience</strong> - Graceful handling of parsing errors and edge cases</li>
<li><strong>Debug support</strong> - Verbose logging for troubleshooting</li>
</ul>
<h2 id="quick-start">Quick Start<a class="headerlink" href="#quick-start" title="Permanent link">¶</a></h2>
<p>Install the plugin:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a>pip<span class="w"> </span>install<span class="w"> </span>mkdocs-output-as-input
</code></pre></div>
<p>Add to your <code>mkdocs.yml</code>:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">stage</span>
<a href="#__codelineno-1-4" id="__codelineno-1-4" name="__codelineno-1-4"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">main</span>
<a href="#__codelineno-1-5" id="__codelineno-1-5" name="__codelineno-1-5"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">article</span>
</code></pre></div>
<p>Build your documentation:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a>mkdocs<span class="w"> </span>build
</code></pre></div>
<p>Find your cousin files in the <code>stage/</code> directory!</p>
<h2 id="next-steps">Next Steps<a class="headerlink" href="#next-steps" title="Permanent link">¶</a></h2>
<ul>
<li><a href="getting-started/">Getting Started</a> - Installation and basic usage</li>
<li><a href="configuration/">Configuration</a> - All plugin options explained</li>
<li><a href="examples/">Examples</a> - Real-world use cases and workflows</li>
<li><a href="api/">API Reference</a> - Technical documentation</li>
</ul>
<h2 id="support">Support<a class="headerlink" href="#support" title="Permanent link">¶</a></h2>
<ul>
<li><a href="https://github.com/vexyart/vexy-mkdocs-output-as-input/issues">GitHub Issues</a></li>
<li><a href="https://github.com/vexyart/vexy-mkdocs-output-as-input/discussions">Discussions</a></li>
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
