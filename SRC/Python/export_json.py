import json
import sys
from parser import parse_sms

input_path = sys.argv[1]
output_path = "parsed_sms.json"

parsed = parse_sms(input_path)

with open(output_path, "w") as f:
    json.dump(parsed, f, indent=4)

print("[OK] Export JSON -> parsed_sms.json")
