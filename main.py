import json
from pprint import pprint
from datetime import datetime

with open("db/template.json", "r") as file_in:
    records = json.load(file_in)
pprint(records)

# for i in records:
#     print(i)
# 

def add_day():
    name = input()
    names = records.keys()
    if name in names:
        if records[name]["enabled_time"] == "yes" and \
            records[name]["enabled_count"] == "yes":
            time = input('Write time: ')
            count = input('Write count: ')
            today = datetime.today().strftime('%Y-%m-%d')
            records[name]['current_attempt'][today] = [time, count]
        else if records[name]["enabled_time"] == "yes" and \
            records[name]["enabled_count"] == "no":
            time = input('Write time: ')
            today = datetime.today().strftime('%Y-%m-%d')
            records[name]['current_attempt'][today] = time
        else:
            today = datetime.today().strftime('%Y-%m-%d')
            records[name]['current_attempt'][1] = today
    else:
        print("Please create habit.")
