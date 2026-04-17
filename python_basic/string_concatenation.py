# first ="Hello"
# second="World"

# result=first+""+second
# print(result)
# F string
# name="Rudransh"
# role="Developer"
# result=f"{name} is a {role}"
# print(result)

# words=["Hello", "World" ,"Python"]
# for i in range(len(words)):
#     print(words[i])

# text="Hello World"
# print(text.find("World"))
# print(text.find("xyz"))

text="Hello World"
pos=text.find("World")
if pos!=-1:
    print(f"Found at index{pos}")
else:
    print("Not found")
    