# def work(action):
#     print(f"pls{action}")

# work(" code ")

# Default Arguments
# def greet(name,msg="Good Morning"):
#     print(f"{msg} {name}")


# greet("Rudransh")

# Multiple positional arguments
# def maximum(*args):
#     for a in args:
#         print(a)
#     print(type(args))
#     return max(args)

# print(maximum(1,3,2,10,9))

# args is a Tuple internally
# **kwargs
# def show_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}={value}")
#     print(type(kwargs))    

# show_info(name="Rudransh",age=24,city="Mumbai")


# individual *args
# def minimum(*args):
#     for m in args:
#         print(m)
#     return min(args)


# print(minimum(1,3,4,5,6,7,8,9))


# Keyword only
# def employee(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
#     print(type(kwargs))    

# employee(name="Rudransh",age=23,city="Mumbai",Emp_id=620710)

# Combined args and kwargs
# def pizza(price,*toppings,**details):
#     print(f"MRP: {price}")
#     if toppings:
#         for t in toppings:
#             print(t)
#             price+=10
#     for key,value in details.items():
#         print(f"{key}:{value}")
#     print(f"Totalprice:{price}")       

# pizza(110,"Capsicum","Onion","Tomato","Panner",Order_No="1103",Size="Small",Quantity=1)


