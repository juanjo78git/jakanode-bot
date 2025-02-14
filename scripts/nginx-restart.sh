#!/bin/bash

# Check Nginx configuration
echo "Checking Nginx configuration..."
if nginx -t; then
    echo "Valid configuration. Reloading Nginx..."
    systemctl reload nginx
    echo "Nginx reloaded successfully."
else
    echo "Nginx configuration error. Please check the previous messages."
    exit 1
fi
