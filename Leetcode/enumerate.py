# fruits=['apple','banana','cherry']

# for index,fruit in enumerate(fruits):
#     print(index,fruit)

# Convert to List of Tuples
fruits=['apple','banana','cherry']
enumerated_list=list(enumerate(fruits))
print(enumerated_list)

fruits=['apple','banana','cherry']
enumerated_list=[[i,fruit] for i , fruit in enumerate(fruits)]
print(enumerated_list)


