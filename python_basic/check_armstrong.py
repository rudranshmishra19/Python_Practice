num=(int(input("Enter a number:")))  #153
print(f"You entered {num}")  #153
rev=0
sum=0
power=1
temp=num
while temp!=0: 
    rev=temp%10   # 153%10 =3
    power=rev**3   #3*3*3 = 27
    sum+=power   # sum+=3  
    temp//=10     

if sum==num:
    print("The number is Armostrong")
else:
    print("The number is not Armstrong")    

