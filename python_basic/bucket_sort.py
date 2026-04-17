def bucket_sort(arr):
    if not arr:
        return arr
    n=len(arr)

    min_val=min(arr)
    max_val=max(arr)

    #Create empty buckets
    buckets=[[] for _ in range(n)]
    

    #Avoid division by zero
    range_val=max_val-min_val+1
    #Distribution elements
    for num in arr:
        index=(num-min_val)*n //range_val
        buckets[index].append(num)
   
    for bucket in buckets:
        bucket.sort()

    result=[]
    for bucket in buckets:
        result.extend(bucket)        
    
    return result


arr=[12,3,4,6,7]
bucket_sort(arr)
print(bucket_sort(arr))