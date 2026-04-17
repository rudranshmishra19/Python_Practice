# x=int(input("Enter the value of x: "))
# if x==1:
#     print("x is 1")
# elif x==3:
#     print("x is 3")
# else:
#     print(f"x is {x}")    
       
x=2
print(x==2) #print True
print(x==3) #print false
print(x>1) #print True
print(x<3) #print True

#Boolean operations
name="Rudransh"
age =22
if name=="Rudransh" and age==22:
    print("your name is Rudransh and you are 22 years old.\n")
if name=="Rudransh" or name=="jeet":
    print("Your name is either Rudransh or jeet")
#in operation 
name ="Rudransh"
if name in["Rudransh"]:
    print("your name is Rudransh")
# if elif and else statement
a=int(input("Enter your age: "))
if(a>=18):
    print("You are eligible for vote")
elif(a<=0):
     print("you are entering invalid age")
else:
    print("you are below the age to vote")     
#is operator
x=[1,2,3]
y=[1,2,3]
print(x==y)  #True
print(x is y) #false
#not operator
print(not False)#   print True
print(not False==False)  # false 

