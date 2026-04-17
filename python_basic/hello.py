# def greet():
#     print("Hello!")

# greet()

# # Function with Parameteres
# def greet(name):
#     print(f"Hello {name}!")

# greet("Rudransh")  #Hello Rudransh!
# # Function with Return Value
# def add(a,b):
#     return a +b
# result=add(5,3)
# print(result)

# Default Arguments
# def greet(name,message="Good morning"):
#     print(f"{message}, {name} !")

# greet("Rudransh")   #Good morning, Rudransh!
# greet("Rudransh", "Good Evening")  #Good evening,Rudransh!

# def add(*nums):
#     return sum(nums)
# add(1,2)
# add(1,2,3,4)

# def show_info(**details):
#     for key, value in details.items():
#         print(f"{key}:{value}")

# show_info(name="Rudransh",age=21,city="India")

# *args and **Kwargs together
# def show(name, *args, **kwargs):
#     print(name)
#     print(args)
#     print(kwargs)

# show("Rudransh", 1,2,3, city="India",role="developer")

# # *args and **Kwargs
# def my_function(*kids):
#     print("The youngest child is "+ kids[2])

# my_function("Emil","Tobias","Linus")

# def my_function(*kids):
#     print("The youngest child is "+ kids[1])

# my_function("Emil","Tobias","Linus")


# *Args
# def my_function(*args):
#     print("Type:",type(args))
#     print("First argument:",args[0])
#     print("Second argument:",args[1])
#     print("All arguments:",args)

# my_function("Emil","Tobias","Linus")

# def fun(*args):
#     return sum(args)
# print(fun(5,10,15))

# # **Kwargs example
# def fun(**kwargs):
#     for k,val in kwargs.items():
#         print(k,val)
# fun(a=1,b=2,c=3)

# def myFun(*argv):
#     for arg in argv:
#         print(arg)
# myFun('Hello','Welcome','to','GreekforGeeks')

# def multiply(*args):
#     result=1
#     for num in args:
#         result *=num
#     return result
# print(multiply(2,3,4))

# Keyword Arguments(**kwargs)
# def fun(**kwargs):
#     for k,val in kwargs.items():
#         print(k,"=",val)
# fun(s1='python',s2='is',s3='Awesome')

# Normal Positional way
def greet(name,message):
    print(f"{message},{name}!")

greet("Rudransh", "Good morning")
