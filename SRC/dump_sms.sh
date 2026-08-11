#!/bin/bash
OUTPUT="sms_dump_$(date +%Y%m%d_%H%M%S).json"
termux-sms-list > "$OUTPUT"
echo "[OK] Dump SMS -> $OUTPUT"
