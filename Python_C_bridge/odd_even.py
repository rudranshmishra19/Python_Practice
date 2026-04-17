#prompt user for input
num=(int(input("Enter a number :")))
 
if num==1: #check if number is 1 
    print(f"The {num} is nor even nor odd") 
elif num%2==0: #even if remainder is 0 
    print(f"The {num} is even")
else:  #odd if remainder left with non zero
    print(f"The {num} is odd")