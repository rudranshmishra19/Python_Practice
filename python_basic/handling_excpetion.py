# while True:
#     try:
#         x=int(input("enter a number:  "))
#         break
#     except ValueError:
#         print("Oops! That was no valid character. Try again....")

# Try and except block

while True:
    try:
        numerator=int(input("Enter the numberator: "))
        denominator=int(input("Enter a denominatior"))
        result=numerator/denominator
        print(result)
        break
    except ValueError:
        print("Error: please enter a valid number")
        break
    except ZeroDivisionError:
        print("Error : Cannot divide by zero")
        break
