num=(int(input("Enter a number:")))  #153
print(f"You entered {num}")  #153\
digits=[int (d) for d in str(num) ]
n=len(digits)
armstrong_sum=sum(d**n for d in digits)
if armstrong_sum==num:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")



               