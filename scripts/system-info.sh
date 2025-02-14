#!/bin/bash

echo "System Summary"
echo "=========================="

echo -e "\n*System Uptime*"
uptime -p

echo -e "\n*CPU Usage*"
cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1 "%"}')
echo -e "CPU Usage: $cpu_usage"

echo -e "\n*Memory Usage and Free Memory*"
free -h | awk 'NR==2{print "Used Memory: " $3 " de " $2 "\nFree Memory: " $4} NR==3{print "Used Swap: " $3 " de " $2 "\nFree Swap: " $4}'

echo -e "\n*Free Disk Space*"
df -h | grep -E '^/dev/' | awk '{print "Device: " $1 "\nnUsed: " $3 " de " $2 "\nFree: " $4}'

echo -e "\n*Open Ports*"
netstat -tuln | grep LISTEN | awk '{print "Port: " $4}'

echo -e "\n*Logged-in Users*"
who | awk '{print "User: " $1 "\nTerminal: " $2 "\nFrom: " $3 " " $4}'

echo "=========================="
echo "End of System Summary"

