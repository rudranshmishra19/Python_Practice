# Template
# [expression for item in iterable if condition ]
# numbers=[1,2,3,4,5,6,7,8]
# abs_sum =sum(abs(x) for x in numbers)
# print(abs_sum)

# num=[x**2 for x in range(10)]
# print(num)

# How do you flatten a nested list
# Nested_list
list_of_lists =[[1,2,3],[4,5,6],[7,8,9]]

# flattened=[]
# for x in list_of_lists:
#     for y in x:
#         flattened.append(y)

# print(flattened)

# Same thing in list comprehension
# flattened_list=[y for x in list_of_lists for y in x]
# print(flattened_list)

# list of tuples 
# Normal Loop version:
# tuples=[]
# for x in range(3):
#     for y in range(3):
#         tuples.append((x,y))
# print(tuples)

# Same things in list comprehension
tuples=[(x,y) for x in range(3) for y in range(3)]
print(tuples)
