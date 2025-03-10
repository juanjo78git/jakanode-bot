#!/bin/bash

default_dev_dir="$FRONT_DEV_DIR"

REPO_DIR="${1:-$default_dev_dir}"

if [ -z "$REPO_DIR" ] ; then
    echo "ERROR: Missing required parameters or environment variables"
    echo "Usage: $0  [REPO_DIR]"
    exit 1
fi

# Check if the directory exists
if [ ! -d "$REPO_DIR" ]; then
    echo "Error: The specified repository directory ($REPO_DIR) does not exist."
    exit 1
fi

# Change to the repository directory
cd "$REPO_DIR" || { echo "Error: Could not access $REPO_DIR"; exit 1; }

# Check if it's a valid Git repository
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
    echo "Error: $REPO_DIR is not a valid Git repository."
    exit 1
fi

BRANCH=$(git rev-parse --abbrev-ref HEAD)

echo "Pushing changes to branch '$BRANCH'..."
git push origin "$BRANCH"

echo "Push completed successfully."
