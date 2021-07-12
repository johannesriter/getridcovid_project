import json
import csv

with open ("dataSource/kuotaVaksin_jaki.json", "r") as f:
    data = json.load(f)
    names = data["data"]

with open ("dataSource/kuotaVaksin_jaki.csv", "w") as f:
    fieldnames = names[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for name in names:
        writer.writerow(name)

# with open ("dataSource/kuotaVaksin_jaki.json") as f:
#     dict_obj = json.loads(f)
# print(dict_obj)

# print(type(dict_obj))
# print
