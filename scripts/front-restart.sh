#!/bin/bash

# The name of the service to manage
SERVICE="${FRONT_SERVICE_NAME:-jakanode-front}"

# Check if the service is active
if systemctl is-active --quiet $SERVICE; then
    echo "Restarting the $SERVICE service..."
    sudo systemctl restart $SERVICE
else
    echo "Starting the $SERVICE service..."
    sudo systemctl start $SERVICE
fi

# Check the status after trying to start/restart the service
if systemctl is-active --quiet $SERVICE; then
    echo "The $SERVICE service is now running."
else
    echo "Failed to start the $SERVICE service. Displaying logs..."
    sudo journalctl -xe -u $SERVICE --no-pager | tail -n 20
    exit 1
fi

# Display the final status of the service
systemctl status $SERVICE --no-pager
