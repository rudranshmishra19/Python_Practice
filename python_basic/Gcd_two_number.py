# num1=(int(input("Enter the first number:")))
# num2=(int(input("Enter the second number")))
# Largest_number=0
# gcd=0
# if num1>num2:
#     Largest_number=num1
# else:
#     Largest_number=num2 

# for i in range(Largest_number,0,-1):
#     if num1%i==0 and num2%i==0:
#         gcd=i
#         break
# print(f"The GCD of given number is {gcd}")

a=25
b=12

while True:
    r=a%b
    if r==0:
        print(f"{b}")
        break
    else:

        a,b=b,r

       
     
