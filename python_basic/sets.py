# my_set={1,2,3}

# # Basic operation
# my_set.add(4)
# my_set.remove(2)
# my_set.discard(10)

# print(my_set)

# 2. Set operations
set1={1,2,3}
set2={3,4,5}

union=set1 | set2
intersection=set1&set2
print(intersection)
print(union)
difference=set1-set2
print(difference)

# 3.Membership testing (why it's fast)
print(3 in set1)  
