#Dictonary of items and their frequency
freq={"apple":3,"banana":5,"mango":2}
#sort by frequency  (value ) in descending order
sorted_items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
print(sorted_items)

# 