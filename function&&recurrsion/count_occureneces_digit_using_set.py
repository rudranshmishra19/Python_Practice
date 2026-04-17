def occureneces(num):
    seen=set()
    duplicate=set()
    for x in num:
        if x in seen:
            duplicate.add(x)
        else:
            seen.add(x)
    return len(duplicate)

num=[1,2,3,2,3,1]
print(occureneces(num))    #Output: 3 unique numbers,but 3 repeats 
       
    
   