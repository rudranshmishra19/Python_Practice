def prime(num):
      
        if num== 0 or num ==1:
           print("No prime number found !!")
           return 
        # prime number upto num  
        print(f"prime number upto {num}")
        for i in range (2 ,num+1):
            #setting all number as prime 
            is_prime=True
            for j in range(2,int (i**0.5)+1):
                if i % j==0:
                   is_prime=False
                   break
            if is_prime:
                print(i,end= ' ')
        print()
num=(int(input("Enter a number you want the prime upto that :")))
prime(num)
