list1=[1,2,3,4,5,6]
list2=["1","10","11","100","101","110"]
cartesian=[(x,y) for x in list1 for y in list2]
print(cartesian)