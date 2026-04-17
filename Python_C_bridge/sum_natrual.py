#prompt user to input a number
num=(int(input("Enter a natural number:")))
i=0
sum=0
#calculate  the sum of first n natrual number
while i<=num:
    sum+=i   # add incrementally 
    i+=1     #increment i 
print(f"The sum of n natural number is {sum}")