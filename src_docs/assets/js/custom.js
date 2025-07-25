// Custom JavaScript for MkDocs Output as Input Documentation

document.addEventListener('DOMContentLoaded', function() {
    // Add copy button feedback
    const copyButtons = document.querySelectorAll('.md-clipboard');
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const originalText = this.innerHTML;
            this.innerHTML = '✓';
            setTimeout(() => {
                this.innerHTML = originalText;
            }, 1000);
        });
    });

    // Smooth scroll for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add terminal copy functionality
    const terminals = document.querySelectorAll('.terminal');
    terminals.forEach(terminal => {
        terminal.addEventListener('click', function() {
            const text = this.textContent.replace('$ ', '');
            navigator.clipboard.writeText(text).then(() => {
                // Show feedback
                const feedback = document.createElement('div');
                feedback.textContent = 'Copied!';
                feedback.style.cssText = 'position: absolute; background: #4caf50; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px;';
                this.appendChild(feedback);
                setTimeout(() => feedback.remove(), 1000);
            });
        });
    });

    // Version selector enhancement
    const versionSelector = document.querySelector('.md-version__current');
    if (versionSelector) {
        versionSelector.addEventListener('click', function() {
            this.classList.toggle('md-version__current--active');
        });
    }

    // Search enhancement - auto-focus on open
    const searchToggle = document.querySelector('[data-md-toggle="search"]');
    if (searchToggle) {
        searchToggle.addEventListener('change', function() {
            if (this.checked) {
                setTimeout(() => {
                    const searchInput = document.querySelector('.md-search__input');
                    if (searchInput) searchInput.focus();
                }, 100);
            }
        });
    }

    // Add loading indicator for code blocks
    const codeBlocks = document.querySelectorAll('pre code');
    codeBlocks.forEach(block => {
        if (block.textContent.length > 1000) {
            block.style.opacity = '0';
            setTimeout(() => {
                block.style.transition = 'opacity 0.3s';
                block.style.opacity = '1';
            }, 100);
        }
    });

    // Analytics event tracking (if enabled)
    if (typeof gtag !== 'undefined') {
        // Track external link clicks
        const externalLinks = document.querySelectorAll('a[href^="http"]:not([href*="' + location.hostname + '"])');
        externalLinks.forEach(link => {
            link.addEventListener('click', function() {
                gtag('event', 'click', {
                    'event_category': 'outbound',
                    'event_label': this.href
                });
            });
        });

        // Track copy button usage
        copyButtons.forEach((button, index) => {
            button.addEventListener('click', function() {
                gtag('event', 'copy_code', {
                    'event_category': 'engagement',
                    'event_label': 'block_' + index
                });
            });
        });
    }
});