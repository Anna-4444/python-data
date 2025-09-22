import json
import re

with open("data.json", "r") as file:
    data = json.load(file)

for item in data:
    item["Category"] = re.split(r"[ .(]", item["Category"])[0]
    # print item["Category"]

print(data)