# num=(int(input("Enter a number :")))
# #now we have to loop from last number
# sum=0
# rev=0
# while num!=0:  
#     rev=num%10   # 478%10 = 8 # 47%10=7
#     sum+=rev   #0+8=8+7
#     num//=10
# print(f"{sum}")
num= input("Enter a number :")
digit_sum=sum(int(digit)for digit in num if digit.isdigit())
print(f"Sum of digits:{digit_sum}")