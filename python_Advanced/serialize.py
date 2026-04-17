import json

data = {
    "name": "John",
    "age":32,
    "City":"Thane"
}
with open("data.json","w") as file:
    json.dump(data,file)



