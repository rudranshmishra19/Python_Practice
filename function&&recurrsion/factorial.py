def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num* factorial( num-1) # recursive step

num=int(input("Enter a number :"))
fact=factorial(num)
print(f"{fact}")