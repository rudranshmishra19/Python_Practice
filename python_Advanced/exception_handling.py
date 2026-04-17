# try:
#     num=(int(input("Enter a number:")))
#     result=10/num
#     print(f"{result}")
# except ZeroDivisionError:
#     print("Divison by zero is invalid")
# except ValueError:
#     print("Invalid input pls enter a number")    

#using else and finally

try:
    file=open("Sequence 01.MP4","r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("file not found!")
else:
    print("File read sucessfully")
finally:
    try:
      file.close()
      print("File closed") 
    except NameError:
        pass                 