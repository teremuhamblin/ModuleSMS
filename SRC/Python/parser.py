import json

def parse_sms(path):
    with open(path, "r") as f:
        data = json.load(f)

    parsed = []
    for sms in data:
        parsed.append({
            "number": sms.get("number"),
            "date": sms.get("date"),
            "body": sms.get("body").strip()
        })

    return parsed
