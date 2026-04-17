num=(int(input("Enter a number :")))
#prompt user to enter a number
for i in range(2,num):
 if num<=1:
    print ("The number is non prime ")    
else:
    for i in range(2,num):
     if num%i==0:
        print(f"The number is non prime {num}")    
        break
       
    else:   
        print(f"The number is prime {num}")