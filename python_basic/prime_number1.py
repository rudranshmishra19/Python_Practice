import math
def prime(num):
    if num==0 or num==1:
        print(f"The number{num} is non prime")
        return False
   
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
        
             return False
       
    return True        


num=(int(input("Enter a number :")))
print(num)
result=prime(num)
if result==True:
    print(f"The number {num} is prime")
else:
    print(f"The number {num} is non prime")
