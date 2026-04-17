# with open("myfile.txt","w") as file:
#     file.write("Hello! This is my first file .\n")
#     if file:
#         print("File created sucessfully")
#     else:
#         print("File is not created ")    

with open("myfile.txt","r") as file:
    contents=file.read()
    print(contents)

# with open("myfile.txt","a") as file:
#     file.write("This is a new line added.\n"



