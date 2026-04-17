def add_logs(func):
    def wrapper():
        print("Starting....")
        func()
        print("Done")
    return wrapper

@add_logs
def greet():
    print("Hello")

greet()
    