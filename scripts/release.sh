#!/bin/bash
# this_file: scripts/release.sh

set -e

# Default to patch release if no version type provided
VERSION_TYPE=${1:-patch}

echo "Preparing release for vexy-mkdocs-output-as-input..."

# Ensure we're in the project root
cd "$(dirname "$0")/.."

# Check if there are uncommitted changes
if ! git diff --quiet HEAD; then
    echo "Error: There are uncommitted changes. Please commit or stash them first."
    exit 1
fi

# Check if we're on main branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "Warning: You're not on the main branch. Current branch: $CURRENT_BRANCH"
    read -p "Do you want to continue? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Get current version from git tags
CURRENT_VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0")
echo "Current version: $CURRENT_VERSION"

# Calculate next version
calculate_next_version() {
    local version=$1
    local type=$2
    
    # Remove 'v' prefix if present
    version=${version#v}
    
    # Split version into parts
    IFS='.' read -r major minor patch <<< "$version"
    
    case $type in
        major)
            major=$((major + 1))
            minor=0
            patch=0
            ;;
        minor)
            minor=$((minor + 1))
            patch=0
            ;;
        patch)
            patch=$((patch + 1))
            ;;
        *)
            echo "Invalid version type: $type. Use major, minor, or patch."
            exit 1
            ;;
    esac
    
    echo "v$major.$minor.$patch"
}

NEXT_VERSION=$(calculate_next_version "$CURRENT_VERSION" "$VERSION_TYPE")
echo "Next version: $NEXT_VERSION"

# Run tests first
echo "Running tests..."
./scripts/test.sh

# Update changelog
echo "Please update CHANGELOG.md with the new version information."
echo "Press Enter when you've updated the changelog..."
read

# Show git status
git status

# Commit any changelog updates
if ! git diff --quiet HEAD; then
    echo "Committing changelog updates..."
    git add CHANGELOG.md
    git commit -m "Update changelog for $NEXT_VERSION"
fi

# Create and push tag
echo "Creating and pushing tag $NEXT_VERSION..."
git tag -a "$NEXT_VERSION" -m "Release $NEXT_VERSION"
git push origin "$NEXT_VERSION"

# Build package
echo "Building package..."
./scripts/build.sh

echo "Release $NEXT_VERSION completed successfully!"
echo "GitHub Actions will automatically publish to PyPI when the tag is detected."