# s="hello"
# i=len(s)//2

# res=s[:i].upper()+s[i:]
# print(res)


# Using loops
# s="hello"
# half_index=len(s)//2
# res=""
# for i in range(len(s)):
#     if i < half_index:
#         res+=s[i].upper()
#     else:
#         res+=s[i]

# print(res)

# List Comprehension
# s="hello"
# index=len(s)//2
# res=''.join([s[i].upper() if i< index else  s[i] for i in range(len(s))])
# print(res)


# List Comprehension
