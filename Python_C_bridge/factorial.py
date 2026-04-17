#prompt user for input
num=(int(input("Enter a number you want the factorial of :")))
i=1  # start with 1 till num
factorial=1  #intialize factorial with 1 so we can start multiply with 1
while i<=num:
    factorial*=i  # store 1*i for first iteration =1x1 =1 then 1*2=2 ,2*3=6,6*4=24 and so on......
    i+=1  #increment i 
print(f"The factorial of {num} is {factorial}")    

