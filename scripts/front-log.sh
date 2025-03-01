#!/bin/bash

# The name of the service to manage
SERVICE="${FRONT_SERVICE_NAME:-jakanode-front}"

# sudo journalctl -xe -u $SERVICE --no-pager | tail -n 5
#
# Display the final status of the service
systemctl status $SERVICE --no-pager
