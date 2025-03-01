#!/bin/bash

# Step 0: Check if required environment variables or params are set
default_service_name="$FRONT_SERVICE_NAME"
default_dev_dir="$FRONT_DEV_DIR"
default_prod_dir="$FRONT_PROD_DIR"

SERVICE_NAME="${1:-$default_service_name}"
DEV_DIR="${2:-$default_dev_dir}"
PROD_DIR="${3:-$default_prod_dir}"

if [ -z "$SERVICE_NAME" ] || [ -z "$DEV_DIR" ] || [ -z "$PROD_DIR" ]; then
    echo "ERROR: Missing required parameters or environment variables"
    echo "Usage: $0 [SERVICE_NAME] [DEV_DIR] [PROD_DIR]"
    exit 1
fi

echo "Starting deployment..."

# Step 1: Sync code from development to production
echo "Syncing files from $DEV_DIR to $PROD_DIR..."
rsync -av --delete \
    --exclude={'venv','.venv','env','.env','.env/','__pycache__','.mypy_cache','.mypy_cache/*','.git','.git/*','.gitignore','.vscode/','.idea/','logs/*','*.log','*.pyc','*.pyo','*.swp','*.swo','*.sqlite3'} \
    --include='logs/.gitkeep' \
    "$DEV_DIR/" "$PROD_DIR/"

# Step 2: Ensure the virtual environment exists
if [ -d "$PROD_DIR/venv" ]; then
    VENV_DIR="$PROD_DIR/venv"
elif [ -d "$PROD_DIR/.venv" ]; then
    VENV_DIR="$PROD_DIR/.venv"
else
    echo "Virtual environment not found. Creating one..."
    python3 -m venv "$PROD_DIR/venv"
    VENV_DIR="$PROD_DIR/venv"
fi

PYTHON_BIN="$VENV_DIR/bin/python"  # Now we can safely assign PYTHON_BIN

# Step 3: Install dependencies
echo "Installing dependencies..."
"$PYTHON_BIN" -m pip install -r "$PROD_DIR/requirements.txt"
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies!"
    exit 1
fi

# Step 4: Run database migrations
echo "Running database migrations..."
"$PYTHON_BIN" -m database.migrate
if [ $? -ne 0 ]; then
    echo "Migration failed! Deployment aborted."
    exit 1
fi

# Step 5: Restart the service
echo "Restarting service: $SERVICE_NAME..."
sudo systemctl restart "$SERVICE_NAME"
if [ $? -ne 0 ]; then
    echo "WARNING: Service restart failed! Check logs."
else
    echo "Deployment completed successfully!"
fi

