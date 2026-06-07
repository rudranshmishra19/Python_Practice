# s="geeksforgeeks"
# res ="".join(dict.fromkeys(s))
# print(res)
# Using OrderedDict.fromkeys()
# using loop with sets 
# s="Rudransh Mishra"
# seen=set()
# res=""
# for char in s:
#     if char not in seen:
#         res+=char
#     seen.add(char)
# print(res)

# using list comphernsion
# s="shivangini mishra"
# x="".join([char for i,char in enumerate (s) if char not in s[:i]])
# print(x)

# Python least Frequenct Character in String

# From collections import Counter


