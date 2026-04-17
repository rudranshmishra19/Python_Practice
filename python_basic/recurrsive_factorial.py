def factorial(num):
  
    if num<0:
      return "Factorial is not defined for negative number"
    elif num==0 or num==1:
       return 1
    else:
        
     return num*factorial(num-1)
    
num=(int(input("Enter a number :")))
result=factorial(num)
print(f"The factorial of given number is {factorial(num)}")      