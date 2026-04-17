#The key to group Anagrams
from collections import defaultdict

# Regular dict 
# groups={}
# for word in ["eat","tea","tan","man","anm","gay","yga"]:
#     key=''.join(sorted(word))
#     if key not in groups:
#         groups[key]=[] #create a list
#     groups[key].append(word)
# print(groups)

#defaultdict (automagic)
groups=defaultdict(tuple)
for word in ["eat","tea","ate","late","alte"]:
    key=''.join(sorted(word))
    groups[key]=groups[key]+(word,)
print(dict(groups))
