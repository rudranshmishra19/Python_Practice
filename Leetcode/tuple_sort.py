freq={'apple':3,'banana':5,'mango':2}
freq_items=freq.items()

for x in freq_items:
    print("Full tuple",x)
    print("x[0] (key):",x[0])
    print("x[1] (value):",x[1])
    print()

print(sorted(freq.items(),key=lambda x:x[1] ,reverse=True))
