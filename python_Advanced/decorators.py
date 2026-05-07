# Function are objects ,can be stored in variable and passed as arguments
# def work():
#     print("coding")

# wr=work
# wr()

# pass function as argument

# def action(ac):
#     ac()

# action(work)


# Function inside a function
# def outer():
#     def inner():
#         print("i am Akatsuki member")
#     inner()

# outer()


# Function can be returned
# def outer():
#     def inner():
#         print("i am inner")
#     return inner

# f=outer()
# f()


# Decorator
def my_habits(func1,func2):
    def wrapper():
        print("wake")
        func1()
        func2()
        print("sleep")
    return wrapper


def work():
    print("code")


def workout():
    print("gym")

# Manual call -@syntax nahi chalegya
my_routine=my_habits(work,workout)
my_routine()
