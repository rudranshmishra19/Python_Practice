#Empty list
my_list=[]

#list of integer
int_list=[1,2,3,4]
print(int_list)
#list with mixed datatype
mixed_list=[1,"Rudransh",4.5,True]
print(mixed_list)
#Nested list
nested_list=[[12],[23],[45]]
print(nested_list)

#operation on list
my_list.append(1)
my_list.append(2)
my_list.append(3)
# print 1 ,2 ,3
for x in my_list:
    print(x)
# remove the last element
my_list.pop()
print(my_list)
my_list.remove(1)
print(my_list)
#combine list
list1=[1,2,3]
list2=[4,5,6]
combined=list1+list2
print(combined)
#slice list
my_list=[10,20,30,40,50]
print(my_list[1:4])
