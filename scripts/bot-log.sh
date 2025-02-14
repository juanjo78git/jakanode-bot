#!/bin/bash

# The name of the service to manage
SERVICE="${SERVICE_NAME:-jakanode-bot}"

# sudo journalctl -xe -u $SERVICE --no-pager | tail -n 5
#
# Display the final status of the service
systemctl status $SERVICE --no-pager
