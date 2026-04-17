def safe_divide(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b


a=5
b=4
print(safe_divide(a,b))
        