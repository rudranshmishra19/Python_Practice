# def occurrences_str(s):
#     freq={}
#     for char in s:
#         freq[char]=freq.get(char,0)+1
#     return freq



# s="banana"
# print(occurrences_str(s))


from collections import Counter
print(Counter("banana"))

