import itertools
# list1=[1,2,3]   #using +Operator
# list2=[4,5,6]
# merged=list1+list2
# print(merged)

#Extend methods
# list1=[1,2,3]
# list2=[4,5,65]
# list1.extend(list2)
# print(list1)

#using unpacking 
# list1=[1,2,3]
# list2=[4,5,6]
# merged=[*list1 ,*list2]
# print(merged)

# Using itertools.chain()
list1=[1,2,3]
list2=[4,5,6]
merged=[]
seen=set()
for item in list1+list2:
    if item not in seen:
        merged.append(item)
        seen.add(item)
print(merged)
