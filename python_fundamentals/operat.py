number=(2+8)/5
number1=1+2*3/4.0   # 6/4.0 =      3/2 =   1.5 +1 =2.5
print(number)
print(number1)
#modulo operator
remainder=11%3
print(remainder)
# power 
squared=7**2
cubed=2**3
print(squared)
print(cubed)
# operator with string
str="Hello"+""+"World"
print(str)
str1="Run"+""+"fun"
print(str1)
#operation on list
list=[1,2,3,4]
list2=[5,6,7,8]
combined=list+list2
print(combined)
print([1,2,3]*2)
x=object()  #Create an instance of the object class
y=object()  #Create another instance of the object class

#initalize the list
x_list=[x]*10 #create a list of one instance of x 
y_list=[y]*10 #create a list of one instance of y

#combine both list
big_list=x_list+y_list

print(f"x_list contains {len(x_list)} objects :{x_list}")
print(f"y_list contains {len(y_list)} objects :{y_list}")
print(f"big_list contains {len(big_list)} objects :{big_list}")
# testing code
if x_list.count(x)==10 and y_list.count(y)==10:
    print("Almost there....")
if big_list.count(x)==10 and big_list.count(y)==10:
    print("Great!")    