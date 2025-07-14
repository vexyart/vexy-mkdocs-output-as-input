---
author: Vexy
code_count: 17
date: 2025-01-14
description: A plugin that captures HTML output and creates cousin Markdown files
has_code: true
pipeline_version: '1.0'
processed: true
source: mkdocs-output-as-input
tags:
- mkdocs
- plugin
- documentation
- pipeline
title: MkDocs Output as Input Plugin
version: 1.0.0
---


<div class="md-content__inner md-typeset">
<h1 class="custom-heading" id="vexy-mkdocs-output-as-input">vexy-mkdocs-output-as-input<a class="headerlink" href="#vexy-mkdocs-output-as-input" title="Permanent link">¶</a></h1>
<p><a href="https://pypi.org/project/vexy-mkdocs-output-as-input/"><img alt="PyPI version" src="https://badge.fury.io/py/vexy-mkdocs-output-as-input.svg"/></a>
<a href="https://github.com/vexyart/vexy-mkdocs-output-as-input/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/vexyart/vexy-mkdocs-output-as-input/workflows/CI/badge.svg"/></a>
<a href="https://codecov.io/gh/vexyart/vexy-mkdocs-output-as-input"><img alt="codecov" src="https://codecov.io/gh/vexyart/vexy-mkdocs-output-as-input/branch/main/graph/badge.svg"/></a>
<a href="https://opensource.org/licenses/MIT"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"/></a>
<a href="https://pypi.org/project/vexy-mkdocs-output-as-input/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/vexy-mkdocs-output-as-input.svg"/></a></p>
<p>A MkDocs plugin that captures HTML output and creates "cousin" Markdown files with original frontmatter and extracted HTML content.</p>
<h2 class="custom-heading" id="features">Features<a class="headerlink" href="#features" title="Permanent link">¶</a></h2>
<p>This plugin enables powerful post-processing workflows by:</p>
<ol>
<li>✅ Preserving your original Markdown structure and frontmatter</li>
<li>✅ Capturing the fully-rendered HTML output from MkDocs</li>
<li>✅ Creating new Markdown files that combine original metadata with processed HTML</li>
<li>✅ Enabling further processing by other static site generators</li>
</ol>
<h2 class="custom-heading" id="installation">Installation<a class="headerlink" href="#installation" title="Permanent link">¶</a></h2>
<p>Install from PyPI:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a>uv<span class="w"> </span>pip<span class="w"> </span>install<span class="w"> </span>--system<span class="w"> </span>--upgrade<span class="w"> </span>vexy-mkdocs-output-as-input
</code></pre></div>
<p>Or install from source:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a>pip<span class="w"> </span>install<span class="w"> </span>git+https://github.com/vexyart/vexy-mkdocs-output-as-input
</code></pre></div>
<h2 class="custom-heading" id="quick-start">Quick Start<a class="headerlink" href="#quick-start" title="Permanent link">¶</a></h2>
<p>Add the plugin to your <code>mkdocs.yml</code>:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-2-2" id="__codelineno-2-2" name="__codelineno-2-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">search</span><span class="w">  </span><span class="c1"># Other plugins</span>
<a href="#__codelineno-2-3" id="__codelineno-2-3" name="__codelineno-2-3"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">output-as-input</span>
</code></pre></div>
<p>Build your site:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a>mkdocs<span class="w"> </span>build
</code></pre></div>
<p>Find your processed files in the <code>stage/</code> directory (relative to your MkDocs project root).</p>
<h2 class="custom-heading" id="configuration">Configuration<a class="headerlink" href="#configuration" title="Permanent link">¶</a></h2>
<p>All configuration options with their defaults:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-4-3" id="__codelineno-4-3" name="__codelineno-4-3"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">stage</span><span class="w">          </span><span class="c1"># Output directory name (default: 'stage')</span>
<a href="#__codelineno-4-4" id="__codelineno-4-4" name="__codelineno-4-4"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">main</span><span class="w">        </span><span class="c1"># HTML element to extract (default: 'main')</span>
<a href="#__codelineno-4-5" id="__codelineno-4-5" name="__codelineno-4-5"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">article</span><span class="w">       </span><span class="c1"># Tag to use in output (default: 'article')</span>
<a href="#__codelineno-4-6" id="__codelineno-4-6" name="__codelineno-4-6"></a><span class="w">      </span><span class="nt">verbose</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">false</span><span class="w">            </span><span class="c1"># Enable verbose logging (default: false)</span>
</code></pre></div>
<h3 class="custom-heading" id="options-explained">Options Explained<a class="headerlink" href="#options-explained" title="Permanent link">¶</a></h3>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>stage_dir</code></td>
<td>string</td>
<td><code>"stage"</code></td>
<td>Directory name for output files (relative to project root)</td>
</tr>
<tr>
<td><code>html_element</code></td>
<td>string</td>
<td><code>"main"</code></td>
<td>CSS selector for the HTML element to extract</td>
</tr>
<tr>
<td><code>target_tag</code></td>
<td>string</td>
<td><code>"article"</code></td>
<td>HTML tag to use in the output (replaces extracted element's tag)</td>
</tr>
<tr>
<td><code>verbose</code></td>
<td>boolean</td>
<td><code>false</code></td>
<td>Enable detailed logging for debugging</td>
</tr>
</tbody>
</table>
<h2 class="custom-heading" id="how-it-works">How It Works<a class="headerlink" href="#how-it-works" title="Permanent link">¶</a></h2>
<h3 class="custom-heading" id="input-process-output">Input → Process → Output<a class="headerlink" href="#input-process-output" title="Permanent link">¶</a></h3>
<ol>
<li>
<p><strong>Input</strong>: Your source Markdown with frontmatter
   <div class="highlight"><pre><span></span><code><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a>---
<a href="#__codelineno-5-2" id="__codelineno-5-2" name="__codelineno-5-2"></a>title: My Page
<a href="#__codelineno-5-3" id="__codelineno-5-3" name="__codelineno-5-3"></a><span class="gu">author: Jane Doe</span>
<a href="#__codelineno-5-4" id="__codelineno-5-4" name="__codelineno-5-4"></a><span class="gu">---</span>
<a href="#__codelineno-5-5" id="__codelineno-5-5" name="__codelineno-5-5"></a>
<a href="#__codelineno-5-6" id="__codelineno-5-6" name="__codelineno-5-6"></a><span class="gh"># My Page</span>
<a href="#__codelineno-5-7" id="__codelineno-5-7" name="__codelineno-5-7"></a>
<a href="#__codelineno-5-8" id="__codelineno-5-8" name="__codelineno-5-8"></a>This is my content with <span class="gs">**markdown**</span>.
</code></pre></div></p>
</li>
<li>
<p><strong>MkDocs Processing</strong>: Renders to HTML as usual
   <div class="highlight"><pre><span></span><code><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a><span class="p">&lt;</span><span class="nt">main</span> <span class="na">class</span><span class="o">=</span><span class="s">"md-content"</span><span class="p">&gt;</span>
<a href="#__codelineno-6-2" id="__codelineno-6-2" name="__codelineno-6-2"></a>  <span class="p">&lt;</span><span class="nt">h1</span><span class="p">&gt;</span>My Page<span class="p">&lt;/</span><span class="nt">h1</span><span class="p">&gt;</span>
<a href="#__codelineno-6-3" id="__codelineno-6-3" name="__codelineno-6-3"></a>  <span class="p">&lt;</span><span class="nt">p</span><span class="p">&gt;</span>This is my content with <span class="p">&lt;</span><span class="nt">strong</span><span class="p">&gt;</span>markdown<span class="p">&lt;/</span><span class="nt">strong</span><span class="p">&gt;</span>.<span class="p">&lt;/</span><span class="nt">p</span><span class="p">&gt;</span>
<a href="#__codelineno-6-4" id="__codelineno-6-4" name="__codelineno-6-4"></a><span class="p">&lt;/</span><span class="nt">main</span><span class="p">&gt;</span>
</code></pre></div></p>
</li>
<li>
<p><strong>Output</strong>: Cousin file with preserved frontmatter + extracted HTML
   <div class="highlight"><pre><span></span><code><a href="#__codelineno-7-1" id="__codelineno-7-1" name="__codelineno-7-1"></a>---
<a href="#__codelineno-7-2" id="__codelineno-7-2" name="__codelineno-7-2"></a>title: My Page
<a href="#__codelineno-7-3" id="__codelineno-7-3" name="__codelineno-7-3"></a><span class="gu">author: Jane Doe</span>
<a href="#__codelineno-7-4" id="__codelineno-7-4" name="__codelineno-7-4"></a><span class="gu">---</span>
<a href="#__codelineno-7-5" id="__codelineno-7-5" name="__codelineno-7-5"></a>
<a href="#__codelineno-7-6" id="__codelineno-7-6" name="__codelineno-7-6"></a>&lt;article class="md-content"&gt;
<a href="#__codelineno-7-7" id="__codelineno-7-7" name="__codelineno-7-7"></a>  &lt;h1&gt;My Page&lt;/h1&gt;
<a href="#__codelineno-7-8" id="__codelineno-7-8" name="__codelineno-7-8"></a>  &lt;p&gt;This is my content with &lt;strong&gt;markdown&lt;/strong&gt;.&lt;/p&gt;
<a href="#__codelineno-7-9" id="__codelineno-7-9" name="__codelineno-7-9"></a>&lt;/article&gt;
</code></pre></div></p>
</li>
</ol>
<h2 class="custom-heading" id="use-cases">Use Cases<a class="headerlink" href="#use-cases" title="Permanent link">¶</a></h2>
<h3 class="custom-heading" id="multi-stage-documentation-pipeline">🔄 Multi-Stage Documentation Pipeline<a class="headerlink" href="#multi-stage-documentation-pipeline" title="Permanent link">¶</a></h3>
<p>Process documentation through MkDocs first, then feed to another SSG:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-8-1" id="__codelineno-8-1" name="__codelineno-8-1"></a><span class="c1"># mkdocs.yml</span>
<a href="#__codelineno-8-2" id="__codelineno-8-2" name="__codelineno-8-2"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-8-3" id="__codelineno-8-3" name="__codelineno-8-3"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-8-4" id="__codelineno-8-4" name="__codelineno-8-4"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">hugo/content</span>
<a href="#__codelineno-8-5" id="__codelineno-8-5" name="__codelineno-8-5"></a>
<a href="#__codelineno-8-6" id="__codelineno-8-6" name="__codelineno-8-6"></a><span class="c1"># Then run:</span>
<a href="#__codelineno-8-7" id="__codelineno-8-7" name="__codelineno-8-7"></a><span class="c1"># mkdocs build &amp;&amp; hugo build</span>
</code></pre></div>
<h3 class="custom-heading" id="content-extraction">📝 Content Extraction<a class="headerlink" href="#content-extraction" title="Permanent link">¶</a></h3>
<p>Extract just the article content without theme wrapper:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-9-1" id="__codelineno-9-1" name="__codelineno-9-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-9-2" id="__codelineno-9-2" name="__codelineno-9-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-9-3" id="__codelineno-9-3" name="__codelineno-9-3"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">article</span>
<a href="#__codelineno-9-4" id="__codelineno-9-4" name="__codelineno-9-4"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">div</span>
</code></pre></div>
<h3 class="custom-heading" id="custom-post-processing">🎨 Custom Post-Processing<a class="headerlink" href="#custom-post-processing" title="Permanent link">¶</a></h3>
<p>Preserve MkDocs rendering while preparing for custom templates:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-10-1" id="__codelineno-10-1" name="__codelineno-10-1"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-10-2" id="__codelineno-10-2" name="__codelineno-10-2"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-10-3" id="__codelineno-10-3" name="__codelineno-10-3"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">_includes</span>
<a href="#__codelineno-10-4" id="__codelineno-10-4" name="__codelineno-10-4"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">main</span>
<a href="#__codelineno-10-5" id="__codelineno-10-5" name="__codelineno-10-5"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">section</span>
</code></pre></div>
<h2 class="custom-heading" id="examples">Examples<a class="headerlink" href="#examples" title="Permanent link">¶</a></h2>
<h3 class="custom-heading" id="basic-example">Basic Example<a class="headerlink" href="#basic-example" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-11-1" id="__codelineno-11-1" name="__codelineno-11-1"></a><span class="c1"># mkdocs.yml</span>
<a href="#__codelineno-11-2" id="__codelineno-11-2" name="__codelineno-11-2"></a><span class="nt">site_name</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">My Documentation</span>
<a href="#__codelineno-11-3" id="__codelineno-11-3" name="__codelineno-11-3"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-11-4" id="__codelineno-11-4" name="__codelineno-11-4"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">output-as-input</span>
</code></pre></div>
<h3 class="custom-heading" id="advanced-example">Advanced Example<a class="headerlink" href="#advanced-example" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-12-1" id="__codelineno-12-1" name="__codelineno-12-1"></a><span class="c1"># mkdocs.yml</span>
<a href="#__codelineno-12-2" id="__codelineno-12-2" name="__codelineno-12-2"></a><span class="nt">site_name</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">My Documentation</span>
<a href="#__codelineno-12-3" id="__codelineno-12-3" name="__codelineno-12-3"></a><span class="nt">theme</span><span class="p">:</span>
<a href="#__codelineno-12-4" id="__codelineno-12-4" name="__codelineno-12-4"></a><span class="w">  </span><span class="nt">name</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">material</span>
<a href="#__codelineno-12-5" id="__codelineno-12-5" name="__codelineno-12-5"></a>
<a href="#__codelineno-12-6" id="__codelineno-12-6" name="__codelineno-12-6"></a><span class="nt">plugins</span><span class="p">:</span>
<a href="#__codelineno-12-7" id="__codelineno-12-7" name="__codelineno-12-7"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">search</span>
<a href="#__codelineno-12-8" id="__codelineno-12-8" name="__codelineno-12-8"></a><span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">output-as-input</span><span class="p">:</span>
<a href="#__codelineno-12-9" id="__codelineno-12-9" name="__codelineno-12-9"></a><span class="w">      </span><span class="nt">stage_dir</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">processed</span>
<a href="#__codelineno-12-10" id="__codelineno-12-10" name="__codelineno-12-10"></a><span class="w">      </span><span class="nt">html_element</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">article.md-content__inner</span>
<a href="#__codelineno-12-11" id="__codelineno-12-11" name="__codelineno-12-11"></a><span class="w">      </span><span class="nt">target_tag</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">main</span>
<a href="#__codelineno-12-12" id="__codelineno-12-12" name="__codelineno-12-12"></a><span class="w">      </span><span class="nt">verbose</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">true</span>
<a href="#__codelineno-12-13" id="__codelineno-12-13" name="__codelineno-12-13"></a>
<a href="#__codelineno-12-14" id="__codelineno-12-14" name="__codelineno-12-14"></a><span class="c1"># Process specific content area from Material theme</span>
</code></pre></div>
<h3 class="custom-heading" id="integration-example">Integration Example<a class="headerlink" href="#integration-example" title="Permanent link">¶</a></h3>
<p>Using with other tools in a documentation pipeline:</p>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-13-1" id="__codelineno-13-1" name="__codelineno-13-1"></a><span class="ch">#!/bin/bash</span>
<a href="#__codelineno-13-2" id="__codelineno-13-2" name="__codelineno-13-2"></a><span class="c1"># build.sh</span>
<a href="#__codelineno-13-3" id="__codelineno-13-3" name="__codelineno-13-3"></a>
<a href="#__codelineno-13-4" id="__codelineno-13-4" name="__codelineno-13-4"></a><span class="c1"># Stage 1: Build with MkDocs + plugins</span>
<a href="#__codelineno-13-5" id="__codelineno-13-5" name="__codelineno-13-5"></a>mkdocs<span class="w"> </span>build
<a href="#__codelineno-13-6" id="__codelineno-13-6" name="__codelineno-13-6"></a>
<a href="#__codelineno-13-7" id="__codelineno-13-7" name="__codelineno-13-7"></a><span class="c1"># Stage 2: Process staged output</span>
<a href="#__codelineno-13-8" id="__codelineno-13-8" name="__codelineno-13-8"></a>python<span class="w"> </span>post_process.py<span class="w"> </span>stage/
<a href="#__codelineno-13-9" id="__codelineno-13-9" name="__codelineno-13-9"></a>
<a href="#__codelineno-13-10" id="__codelineno-13-10" name="__codelineno-13-10"></a><span class="c1"># Stage 3: Build final site</span>
<a href="#__codelineno-13-11" id="__codelineno-13-11" name="__codelineno-13-11"></a>hugo<span class="w"> </span>--contentDir<span class="o">=</span>stage/
</code></pre></div>
<h2 class="custom-heading" id="development">Development<a class="headerlink" href="#development" title="Permanent link">¶</a></h2>
<h3 class="custom-heading" id="setup-development-environment">Setup Development Environment<a class="headerlink" href="#setup-development-environment" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-14-1" id="__codelineno-14-1" name="__codelineno-14-1"></a><span class="c1"># Clone the repository</span>
<a href="#__codelineno-14-2" id="__codelineno-14-2" name="__codelineno-14-2"></a>git<span class="w"> </span>clone<span class="w"> </span>https://github.com/vexyart/vexy-mkdocs-output-as-input
<a href="#__codelineno-14-3" id="__codelineno-14-3" name="__codelineno-14-3"></a><span class="nb">cd</span><span class="w"> </span>vexy-mkdocs-output-as-input
<a href="#__codelineno-14-4" id="__codelineno-14-4" name="__codelineno-14-4"></a>
<a href="#__codelineno-14-5" id="__codelineno-14-5" name="__codelineno-14-5"></a><span class="c1"># Create virtual environment</span>
<a href="#__codelineno-14-6" id="__codelineno-14-6" name="__codelineno-14-6"></a>python<span class="w"> </span>-m<span class="w"> </span>venv<span class="w"> </span>venv
<a href="#__codelineno-14-7" id="__codelineno-14-7" name="__codelineno-14-7"></a><span class="nb">source</span><span class="w"> </span>venv/bin/activate<span class="w">  </span><span class="c1"># On Windows: venv\Scripts\activate</span>
<a href="#__codelineno-14-8" id="__codelineno-14-8" name="__codelineno-14-8"></a>
<a href="#__codelineno-14-9" id="__codelineno-14-9" name="__codelineno-14-9"></a><span class="c1"># Install in development mode</span>
<a href="#__codelineno-14-10" id="__codelineno-14-10" name="__codelineno-14-10"></a>pip<span class="w"> </span>install<span class="w"> </span>-e<span class="w"> </span>.<span class="o">[</span>dev<span class="o">]</span>
<a href="#__codelineno-14-11" id="__codelineno-14-11" name="__codelineno-14-11"></a>
<a href="#__codelineno-14-12" id="__codelineno-14-12" name="__codelineno-14-12"></a><span class="c1"># Install pre-commit hooks</span>
<a href="#__codelineno-14-13" id="__codelineno-14-13" name="__codelineno-14-13"></a>pre-commit<span class="w"> </span>install
</code></pre></div>
<h3 class="custom-heading" id="running-tests">Running Tests<a class="headerlink" href="#running-tests" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-15-1" id="__codelineno-15-1" name="__codelineno-15-1"></a><span class="c1"># Run all tests</span>
<a href="#__codelineno-15-2" id="__codelineno-15-2" name="__codelineno-15-2"></a>pytest
<a href="#__codelineno-15-3" id="__codelineno-15-3" name="__codelineno-15-3"></a>
<a href="#__codelineno-15-4" id="__codelineno-15-4" name="__codelineno-15-4"></a><span class="c1"># Run with coverage</span>
<a href="#__codelineno-15-5" id="__codelineno-15-5" name="__codelineno-15-5"></a>pytest<span class="w"> </span>--cov<span class="o">=</span>mkdocs_output_as_input<span class="w"> </span>--cov-report<span class="o">=</span>html
<a href="#__codelineno-15-6" id="__codelineno-15-6" name="__codelineno-15-6"></a>
<a href="#__codelineno-15-7" id="__codelineno-15-7" name="__codelineno-15-7"></a><span class="c1"># Run specific test</span>
<a href="#__codelineno-15-8" id="__codelineno-15-8" name="__codelineno-15-8"></a>pytest<span class="w"> </span>tests/test_plugin.py::TestOutputAsInputPlugin::test_default_config
</code></pre></div>
<h3 class="custom-heading" id="code-quality">Code Quality<a class="headerlink" href="#code-quality" title="Permanent link">¶</a></h3>
<div class="highlight"><pre><span></span><code><a href="#__codelineno-16-1" id="__codelineno-16-1" name="__codelineno-16-1"></a><span class="c1"># Format code</span>
<a href="#__codelineno-16-2" id="__codelineno-16-2" name="__codelineno-16-2"></a>black<span class="w"> </span>src<span class="w"> </span>tests
<a href="#__codelineno-16-3" id="__codelineno-16-3" name="__codelineno-16-3"></a>
<a href="#__codelineno-16-4" id="__codelineno-16-4" name="__codelineno-16-4"></a><span class="c1"># Lint code</span>
<a href="#__codelineno-16-5" id="__codelineno-16-5" name="__codelineno-16-5"></a>ruff<span class="w"> </span>check<span class="w"> </span>src<span class="w"> </span>tests
<a href="#__codelineno-16-6" id="__codelineno-16-6" name="__codelineno-16-6"></a>
<a href="#__codelineno-16-7" id="__codelineno-16-7" name="__codelineno-16-7"></a><span class="c1"># Type check</span>
<a href="#__codelineno-16-8" id="__codelineno-16-8" name="__codelineno-16-8"></a>mypy<span class="w"> </span>src
</code></pre></div>
<h2 class="custom-heading" id="contributing">Contributing<a class="headerlink" href="#contributing" title="Permanent link">¶</a></h2>
<p>Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.</p>
<ol>
<li>Fork the repository</li>
<li>Create your feature branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
<li>Commit your changes (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
<li>Push to the branch (<code>git push origin feature/AmazingFeature</code>)</li>
<li>Open a Pull Request</li>
</ol>
<h2 class="custom-heading" id="license">License<a class="headerlink" href="#license" title="Permanent link">¶</a></h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
<h2 class="custom-heading" id="support">Support<a class="headerlink" href="#support" title="Permanent link">¶</a></h2>
<ul>
<li>📧 Email: you@example.com</li>
<li>🐛 Issues: <a href="https://github.com/vexyart/vexy-mkdocs-output-as-input/issues">GitHub Issues</a></li>
<li>💬 Discussions: <a href="https://github.com/vexyart/vexy-mkdocs-output-as-input/discussions">GitHub Discussions</a></li>
</ul>
</div>
