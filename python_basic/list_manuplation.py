# a=[1,2,3,4]
# b=a
# b.append(a)
# print(a)

# a=[1,2,3]
# b=a.copy()
# b.append(4)
# print(a)
# print(b)
# nested list trap
# a=[[1,2], [3,4]]
# b=a.copy()
# b[0].append(99)
# print(a)

# a=[[0] * 3] *3
# a[0][0]=1
# print(a)
# print(id(a[0]))
# print(id(a[1]))
# print(id(a[2]))

# a=[[0]*3 for _ in range(3)]
# a[0][0]=1
# print(a)
# print(id(a[0]))
# print(id(a[1]))
# print(id(a[2]))

# Modifying while iterating
# a=[1,2,3,4]
# for i in a:
#     if i%2 ==0:
#         a.remove(i)

# print(a)

# List comphernsion
# a=[1,2,3,4]
# # a=[i for i in a if i%2!=0]
# # print(a)

# a=[i for i in a if i%2!=0]
# print(a)
# [expression for item in iterable if condition]
# [expression for item in iterable if condition]
# [expression for item in iterable if condition]
# [expresiion for item in iterblae if condition]
#Normal way 
# a =[]
# for i in range(5):
#     a.append(i)
# print(a)

# a=[i for i in range(5)]
# print(a)

#with condition list comphension
# a=[i for i in range(10) if i%2==0]
# print(a)

#Apply Operation
# a=[i*i for i in range(4)]
# print(a)

#if else in list comphernsion
# a=["even" if i%2 ==0 else "odd" for i in range(5)]
# print(a)

# a=["even" if i%2==0 else "odd" for i in range(5)]
# print(a)

# Nested list Comprehension
# a=[[i*j for j in range(3)] for i in range(3)]
# print(a)

# # Exiting list
# nums=[1,2,3,4,5]
# squared=[x*x for x in nums]
# print(squared)

# #Flatten a list
# a=[[1,2],[3,4],[5,6]]
# flat=[item for sublist in a for item in sublist]
# print(flat)


# a=[i for i in range(5)]
# b=a
# b[0]=99
# print(a)

# a=[i if i%2==0 else -i for i in range(5)]
# print(a)

# Append vs Extend
# a=[1,2]
# b=[3,4]
# a.append(b)
# print(a)

