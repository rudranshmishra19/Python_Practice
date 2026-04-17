n=int(input("Enter the Nth series:"))
fib0=0
fib1=1
#handle edge case
if n<=0:
    print("pls enter a postive integer")
    exit()
if n==1:
    print(f"The Nth series is {fib0}")    
    exit()

print(f"The nth series is {fib0} ,{fib1}",end="")

for i in range(2,n):
      nextfib=fib0+fib1
      print(f", {nextfib}",end="")
      fib0=fib1
      fib1=nextfib

print()
