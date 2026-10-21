import json

f = open('students.json')
data = json.load(f)
mx = -100
name = ''
for i in data:
    i["passed"] = (i["score"] > 80)
    if i["score"] > mx:
        mx = i["score"]
        name = i["name"]
answer5 = open("answer5.json", 'w')
json.dump(data, answer5)
print(name)