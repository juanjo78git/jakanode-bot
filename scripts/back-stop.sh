#!/bin/bash

# The name of the service to stop
SERVICE="${BACK_SERVICE_NAME:-jakanode-back}"

# Check if the service is running
if systemctl is-active --quiet $SERVICE; then
    echo "Stopping the $SERVICE service..."
    sudo systemctl stop $SERVICE
else
    echo "The $SERVICE service is not running."
    exit 0
fi

# Check the status after stopping the service
if systemctl is-active --quiet $SERVICE; then
    echo "Failed to stop the $SERVICE service."
    sudo journalctl -xe -u $SERVICE --no-pager | tail -n 20
    exit 1
else
    echo "The $SERVICE service has been stopped successfully."
fi

# Display the final status of the service
systemctl status $SERVICE --no-pager
