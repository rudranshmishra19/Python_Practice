# s="hello world"
# # Split s into words
# words=s.split()
# # Process each word in the list 'words'
# res=''.join([
#     # if the word has more than 1 character
#       i[0].upper()+i[1:-1]+i[-1].upper()
#       if len(i)>1 else i.upper()

#       for i in words

# ])
# print(res)
# s="welcome to geeksforgeeks"
# res =' '.join(
#     map(
#         lambda word: word[0].upper()+word[1:1]+word[-1].upper()

#     )
# )
# import re
# s="hello world"
# res=re.sub(r'\b(\w) (\w*) (\w) \b',
#            lambda match: match.group(1).upper()
#            +match.group(2)
#            +match.group(3).upper(),
           
#            s)
# print(res)

