#define recurssive function to add to number
def add_numbers_recursive(x,y):
    if y==0:
        return x
    else:
        return add_numbers_recursive(x+1,y-1)

#taking input from user
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

result=add_numbers_recursive(num1,num2)
print(result)