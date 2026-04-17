# list1=['a','b','c']
# index_map={val: i for i,val in enumerate(list1)}
# print(index_map)

list2=['Rudransh','Govind','Mukund']
list2.append('jeet')
list2[0]="Mom"
index_map={val:i for i,val in enumerate(list2)}
print(index_map)
print(index_map["Mom"])
# get to hanlde missing keys 
print(index_map.get("Rudransh","Not found "))
