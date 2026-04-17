def first_repeat_index(nums):
    seen={}
    for i,num in enumerate(nums):
        if num in seen:
            return [seen[num],i] #First and second occurence 
        seen[num]=i
    return []
print(first_repeat_index([4,5,2,4,7])) 
    
