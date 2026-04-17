# num=(int(input("Enter a number :")))

# if num%2==0:
#     print("The number is even")    
# else:
#     print("The number is odd")
    
# Using a function

def check_even_odd(num):
    if num%2==0:
        return"Even"
    else:
        return "Odd"
num=int(input("Enter a number :"))
print(f"The number is {check_even_odd(num)}")    



