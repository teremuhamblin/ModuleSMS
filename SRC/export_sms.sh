#!/bin/bash
INPUT="$1"
OUTPUT="export_sms.csv"
jq -r '.[] | [.number, .date, .body] | @csv' "$INPUT" > "$OUTPUT"
echo "[OK] Export CSV -> $OUTPUT"
