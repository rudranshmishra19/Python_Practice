print(set("my name is rudransh and my name is jeet".split()))
a=set(["Rudransh","jeet","Omkar","Tonge"])
print(a)
b=set(["Mishra","Nakrani","Tonge","Omkar","Rudransh"])
print(b)
# print(a.union(b))
print(a.intersection(b))  # to check common name 
print(b.intersection(a))
# to check the name that not similiar 
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
# to check a name which has a occurence just one time 
print(a.difference(b))
print(b.difference(a))