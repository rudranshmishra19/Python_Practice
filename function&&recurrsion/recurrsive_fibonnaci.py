def fib(num):
    if num==0:
         return 0
    elif num==1:
         return 1       
    else:
         return  fib(num-1) + fib(num-2)

# print full sequence 
terms=int(input("Enter number of terms: "))
print("Fibonacci sequence :")
for i in range(terms):
     print(fib(i),end=" ")


