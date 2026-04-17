def first_repeat_index(nums):
    seen={}
    for i ,num in enumerate(nums):
        if num in seen:
            return [seen[num],i] #first and second occurence
        seen[num]=i #store the index of num
    return []
    
print(first_repeat_index([3,4,5,6,5]))