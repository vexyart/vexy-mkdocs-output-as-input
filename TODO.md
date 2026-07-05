# TODO List for vexy-mkdocs-output-as-input

## 2026 Modernization (done)
- [x] Add GitHub Actions CI (test matrix 3.12/3.13, MkDocs 1.5/1.6 compat, lint job, codecov)
- [x] Add release workflow (build + PyPI trusted publishing + GitHub Release) and dependabot
- [x] Align minimum Python to 3.12 (code uses PEP 695 `type` statements)
- [x] Add end-to-end MkDocs-build integration test on a fixture site
- [x] Document runtime dependencies + BeautifulSoup4 parser choice (`DEPENDENCIES.md`)
- [x] Add `use-cases.md` (Webflow / Docusaurus / plain-HTML pipelines)

## Bigger ideas (parked)
- [ ] Evaluate `selectolax` as a lighter alternative to BeautifulSoup4 for simple
      tag extraction (~1 MB saving), gated on retaining full CSS-selector support.
- [ ] Harden `preserve_links` beyond the current root-relative heuristic (resolve
      links relative to each page's depth in the tree).
- [ ] Add a coverage report artifact / badge refresh once CI is live.

## Phase 1: Documentation Setup
- [x] Create src_docs/ directory structure
- [x] Create src_docs/index.md with landing page content
- [x] Create src_docs/getting-started.md with installation guide
- [x] Create src_docs/configuration.md with detailed config reference
- [x] Create src_docs/examples.md with real-world examples
- [x] Create src_docs/api.md for API documentation
- [x] Create src_docs/development.md with contributing guide
- [x] Create src_docs/faq.md with common questions
- [x] Create src_docs/troubleshooting.md with solutions
- [x] Update mkdocs.yml for src_docs source
- [x] Configure Material theme advanced features
- [x] Set up mkdocstrings for API docs
- [x] Add custom CSS for branding
- [x] Configure social cards generation
- [x] Create build script to output docs/ from src_docs/

## Phase 2: Code Quality Improvements
- [ ] Replace logging with loguru throughout codebase
- [ ] Add structured logging with context
- [ ] Implement custom exception classes
- [ ] Add graceful error degradation
- [ ] Create user-friendly error messages
- [ ] Split plugin.py into modular components
- [ ] Create core.py for main logic
- [ ] Create parser.py for HTML parsing
- [ ] Create writer.py for file writing
- [ ] Create config.py for configuration
- [ ] Create utils.py for utilities
- [ ] Add comprehensive type hints
- [ ] Implement asyncio for parallel processing
- [ ] Add progress indicators
- [ ] Implement file caching mechanism

## Phase 3: Test Suite Enhancement
- [ ] Add integration tests for full pipeline
- [ ] Add theme compatibility tests
- [ ] Add large site performance tests
- [ ] Add multi-plugin interaction tests
- [ ] Add malformed HTML handling tests
- [ ] Add Unicode handling tests
- [ ] Add symlink handling tests
- [ ] Add concurrent processing tests
- [ ] Implement property-based tests with hypothesis
- [ ] Add test fixtures for common scenarios
- [ ] Create test data generators
- [ ] Add performance benchmarks
- [ ] Create visual regression tests
- [ ] Achieve 100% code coverage

## Phase 4: Feature Enhancements
- [ ] Add output_format configuration option
- [ ] Add custom_processors support
- [ ] Add exclude_patterns option
- [ ] Add parallel_processing toggle
- [ ] Add cache_enabled option
- [ ] Add template_engine support
- [ ] Implement smart content extraction
- [ ] Add auto-detection for different themes
- [ ] Improve link resolution logic
- [ ] Add interactive CLI mode
- [ ] Create configuration wizard
- [ ] Add preview mode
- [ ] Add batch processing support

## Phase 5: Developer Experience
- [ ] Create VS Code extension scaffolding
- [ ] Add syntax highlighting for cousin files
- [ ] Create configuration snippets
- [ ] Design reusable GitHub Actions workflow
- [ ] Set up automated testing matrix
- [ ] Add performance regression detection
- [ ] Design plugin extension API
- [ ] Implement hook system
- [ ] Create event-driven architecture
- [ ] Document plugin chaining

## Phase 6: Performance and Scalability
- [ ] Implement content hash-based cache
- [ ] Add incremental processing
- [ ] Support distributed caching
- [ ] Add S3 bucket output support
- [ ] Add Azure Blob storage support
- [ ] Add Google Cloud Storage support
- [ ] Optimize memory usage
- [ ] Add streaming for large files
