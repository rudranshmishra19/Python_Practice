def sum(arr):
    
    sum=0

    for i in arr:
        sum=sum+i
    return(sum)    

arr=[2,3,5]
n=len(arr)
ans=sum(arr)
print('Sum of the array is ',ans)
