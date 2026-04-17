def shout(func):
    def wrapper(name):
        result=func(name)
        return result.upper()
    return wrapper

@shout
def greet(name):
    return f"hello {name}"

print(greet("rudransh"))
