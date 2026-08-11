import json
import sys
from collections import Counter

path = sys.argv[1]

with open(path) as f:
    data = json.load(f)

numbers = Counter([sms["number"] for sms in data])
hours = Counter([sms["date"][11:13] for sms in data])

print("=== STATISTIQUES SMS ===")
print("Top contacts :", numbers.most_common(5))
print("Heures actives :", hours.most_common(5))
