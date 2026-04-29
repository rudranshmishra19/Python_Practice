# my_set={1,2,3}
# print(my_set)

# my_set=set()
# for i in range(1,10):
#      my_set.add(i)
# my_set.pop()
# my_set.pop()

# my_set.discard(11)
# # my_set.remove(5)
# my_set.difference_update({"4"})
# my_set -={6}
# print(my_set)
# your_set=set()
# for i in range(9):
#      your_set.add(i)

# print("my_set:",my_set)
# print("your_set",your_set)
# print("Intersection",my_set.intersection(your_set))
# print("Difference",my_set.difference(your_set))
# print("Union",my_set.union(your_set))
# print("Symetric_difference",my_set.symmetric_difference(your_set))



# length of the set
# print(len(my_set))

# my_list=[1,2,3,4,1]
# my_unique_list=list(set(my_list))
# print(my_unique_list)
t={x**2 for x in [1,2,3,4]}
print(t)
a={x for x in range(3)}
print(a)

# insert element from set t into set a 
a.update(t)
print(a)





