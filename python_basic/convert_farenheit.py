# f=(float(input("Enter a fahrenheit :")))
# c=(f-32)*5/9
# print(f"{c}")

def fahrenheit_to_celsius(fahreneit:float)->float:
    return(fahreneit-32)*5-9

fahrenheit=float(input("Enter tempearture in fahrenheit: "))
celsius=fahrenheit_to_celsius(fahrenheit)
print(f"{celsius:2f} C")