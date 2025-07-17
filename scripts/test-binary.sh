#!/bin/bash
# this_file: scripts/test-binary.sh

set -e

echo "Testing binary creation..."

# Ensure we're in the project root
cd "$(dirname "$0")/.."

# Install dependencies
echo "Installing dependencies..."
uv pip install -e ".[dev,test]"
uv pip install pyinstaller

# Create test binary
echo "Creating test binary..."
uv run pyinstaller --onefile --name mkdocs-output-as-input-test src/mkdocs_output_as_input/cli.py

# Test the binary
echo "Testing binary..."
./dist/mkdocs-output-as-input-test --help

# Create test input
echo "Creating test input..."
mkdir -p test_binary
cat > test_binary/test.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>Test</title></head>
<body>
<main>
<h1>Test Page</h1>
<p>This is a test.</p>
</main>
</body>
</html>
EOF

# Test binary processing
echo "Testing binary processing..."
./dist/mkdocs-output-as-input-test process test_binary/test.html test_binary/output.md

# Verify output
echo "Verifying output..."
if [ -f "test_binary/output.md" ]; then
    echo "✓ Output file created successfully"
    echo "Content:"
    cat test_binary/output.md
else
    echo "✗ Output file not created"
    exit 1
fi

# Cleanup
rm -rf test_binary/
rm -rf build/ dist/ *.spec

echo "Binary test completed successfully!"