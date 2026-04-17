def factorial(num):
    if num<0:
      return "Factorial is not defined for negative number"
    else:
     i=1
     result=1
     while i<=num:
        result *=i
        i+=1
    return result

num=(int(input("Enter a number :")))
result=factorial(num)
if isinstance(result,str):
   print(result)
else:
   
  print(f"The factorail of given number is {factorial(num)}")