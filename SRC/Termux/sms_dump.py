import json
import subprocess
import datetime

output = f"sms_dump_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
raw = subprocess.check_output(["termux-sms-list"])
data = json.loads(raw)

with open(output, "w") as f:
    json.dump(data, f, indent=4)

print("[OK] Dump SMS ->", output)
