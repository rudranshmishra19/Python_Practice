def power(base,exponent):
    if exponent==0:  #base case: anything^0
        return 1     #base case:anything^1 =base
    elif exponent ==1:
        return base
    else:
        return base *power(base,exponent-1)

num=(int(input("Enter a number :")))
print(f"You entered {num}")
exponent=(int(input("Enter the exponent: ")))
result=power(num,exponent)
print(f"{result}")  
