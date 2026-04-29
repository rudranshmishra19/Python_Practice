# # List is Ordered,Mutable,and it allows duplicates
# # my_list=[1,2,2,4]
# # #Uniques methods
# # my_list.append(4)
# # my_list.insert(1,99)
# # print(my_list)
# # my_list.extend([5,6])
# # print(my_list)
# # my_list.remove(2)
# # my_list.pop()
# # print(my_list.count(2))
# # my_list.sort()
# # print(my_list)
# # my_list.reverse()
# # print(my_list)
# # my_list.copy()
# # print(my_list)
# # my_list.clear()
# # print(my_list)

# # Tuples -Ordered,immutable,allow Duplicates
# my_tuple=(1,2,3,4)
# #uniques methods (only 2)
# my_tuple.count(2)
# my_tuple.index(3)  #find index 3
# # Constraints - cannot add remove change element after creatin

# # Sets -Unordered,Mutable,No duplicates
# a={1,2,3}
# a.add(4)
# a.update([7,8]) # 
# a.discard(5)  #no error
# a.remove(1)  #keyerror if value missing
# a.pop() # keyerror if missing
# a.clear()

# b={3,4,5}
# #set opertaions
# a.union(b)
# a.intersection(b)
# a.difference(b)
# a.symmetric_difference(b)
# a.issubset(b)
# a.issuperset(b)
# a.isdisjoint(b)

# # Dictonary -Orderd,multable,uniques keys
# my_dict={"name":"Rudransh","age":23}

# #unique methods
# my_dict.get("name")
# my_dict.get("x","default")
# my_dict.keys()
# my_dict.items()
# my_dict.values()
# my_dict.copy()
# my_dict.clear()
# my_dict.pop("age")
# my_dict.popitem()

# # Common interview Gotchas
# x={}
# x=set()

# #Tuple with one element
# x=(1)
# x=(1,)

# #List cant be dict keys or set elements
# {[1,2]:"val"}
# {[1,2]:"val"}

