import subprocess
import time
import json

print("[INFO] Surveillance SMS active...")

last = None

while True:
    raw = subprocess.check_output(["termux-sms-inbox", "-l", "1"])
    sms = json.loads(raw)[0]

    if sms != last:
        print("[NOUVEAU SMS]", sms)
        last = sms

    time.sleep(2)
