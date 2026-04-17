import json
# Your  Dictionary
data={
    "name":"Rudransh",
    "age":22,
    "skills":["Python","C","SQL"],
    "is_student":False
}


# Store dictionary in  a json file
with open("data.json","w") as json_file:
    json.dump(data,json_file,indent=4)   
    # Indent=4 makes it pretty
