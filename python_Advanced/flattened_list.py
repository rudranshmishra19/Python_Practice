#nested list
nested_list=[[1,2],[3,4],[5,6]]
flattened=[num for sublist in nested_list for num in sublist]
print(flattened)