# colors=('red','green','blue')
# print(colors[0])
# print(colors[-1]) #Last element

# Tuple Packing and Unpacking
# info=('python',3.12,'AI')
# #unpacking
# language,version,topic=info
# print(language)
# print(version)
# print(topic)

# Nested Tuples
# pairs=((1,2),(3,4),(5,6))
# print(pairs[2][1])
# print(pairs[1][1])

# # Use Tuple in Dictonary
# student={
#     ('Ravi',101):'A',
#     ('Anu',102):'B'
# }
# print(student[('Ravi',101)])
# print(student[('Anu',102)])

# Analyze number
def anaylze_numbers(nums):
    min_val=min(nums)
    max_val=max(nums)
    avg_val=sum(nums)/len(nums)
    
    return (min_val,max_val,avg_val)

result=anaylze_numbers([2,5,9,1,4])
print(result)