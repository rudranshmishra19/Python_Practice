# Using replace function
# s = "geeks for geeks"
# res=len(s.replace('g',""))
# print(res)

# Using loop
# s="geeks for geeks"
# res=0
# for c in s:
#     if c!=" ":
#         res+=1
# print(res)

# using loop
# s="Rudransh is a Django Developer"
# res=0
# for c in s:
#     if c!=" ":
#         res+=1
# print(res)

# List Comprehension
# s="Rudransh is a python Developer"
# res=len([c for c in s if c!=" "])
# print(res)
# using regular expression 
# import re
# s="Rudransh is visiting bandra on 27th April"
# res=len(re.sub(r" ","",s))
# print(res)

import re
res= re.sub(r"\s+","","How much can you see through those sharigam of yours")
print(res)

