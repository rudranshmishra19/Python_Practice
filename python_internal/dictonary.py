my_dict={"name":"Rudransh","age":22,"city":"Dombivli"}

del my_dict["name"]
#key check
if "name" in my_dict:
    print("name hain")

if "age" in my_dict:
    print("age hain")

if "city" in my_dict:
    print("....you know")

# my_dict.clear()
print([(x,y) for x,y in my_dict.items()])


