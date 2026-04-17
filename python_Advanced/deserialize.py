import json

with open("data.json","r") as file:
    new_data=json.load(file)

print(new_data)
print(type(new_data))
print(new_data["name"])
