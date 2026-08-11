#!/bin/bash
echo "[INFO] Surveillance SMS..."
while true; do
    termux-sms-inbox -l 1 | jq '.'
    sleep 2
done
