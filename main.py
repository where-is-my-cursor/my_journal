import json
from pprint import pprint

with open("db/template.json", "r") as file_in:
    records = json.load(file_in)
pprint(records)

for i in records:
    print(i)
