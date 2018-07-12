import json

data = {
    "name" : "wangdamei",
    "age" : 22,
    "gender" : "female",
    "mobile" : "1381213123"
}

with open("test.json", "w") as f:
    json.dump(data, f)

with open("test.json", "r") as f:
    d = json.load(f)
    print(d)