list1=[1,2,3,4,5,6]
list2=[7,8,9,10,11,12]
multiply=[(x,y,x*y) for x in list1 for  y in list2]
print(multiply)