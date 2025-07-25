// Custom JavaScript for MkDocs Output as Input documentation

document.addEventListener('DOMContentLoaded', function() {
    // Add copy button to code blocks
    const codeBlocks = document.querySelectorAll('pre > code');
    codeBlocks.forEach(function(codeBlock) {
        // Skip if already has copy button
        if (codeBlock.parentElement.querySelector('.copy-button')) {
            return;
        }
        
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.textContent = 'Copy';
        button.setAttribute('aria-label', 'Copy code to clipboard');
        
        button.addEventListener('click', function() {
            const text = codeBlock.textContent;
            navigator.clipboard.writeText(text).then(function() {
                button.textContent = 'Copied!';
                setTimeout(function() {
                    button.textContent = 'Copy';
                }, 2000);
            });
        });
        
        codeBlock.parentElement.style.position = 'relative';
        codeBlock.parentElement.appendChild(button);
    });
    
    // Initialize tablesort if available
    if (typeof Tablesort !== 'undefined') {
        const tables = document.querySelectorAll('article table');
        tables.forEach(function(table) {
            new Tablesort(table);
        });
    }
});