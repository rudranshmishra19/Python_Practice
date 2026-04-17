# mapping={')':'(','}':'{',']':'['}
# for val in mapping.values():
#     print(val)

# for key,val in mapping.items():
#     print(key,"->",val)
mapping={')':'(','}':'{',']':'['}

for char in  mapping:
    if mapping[char]:
        print(mapping[char])

