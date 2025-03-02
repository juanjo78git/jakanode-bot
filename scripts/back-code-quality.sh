#!/bin/bash

default_dev_dir="$BACK_DEV_DIR"

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

cd "$REPO_DIR"

# Possible virtual environment locations
VENV_DIR=""
if [ -d "$REPO_DIR/venv" ]; then
    VENV_DIR="$REPO_DIR/venv"
elif [ -d "$REPO_DIR/.venv" ]; then
    VENV_DIR="$REPO_DIR/.venv"
else
    echo "Error: No virtual environment found in $REPO_DIR/venv or $REPO_DIR/.venv"
    exit 1
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

echo "Adjusting imports with isort..."
isort .
echo "Formatting code with black..."
black .
echo "Validating static code with pylint..."
pylint .
echo "Validating types with mypy..."
mypy --explicit-package-bases --disable-error-code name-defined .

# Deactivate virtual environment (optional)
deactivate
