def occurrences(num,n):
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            if num[j]==num[i]:
                count+=1
                  
    return count 

num=[1,2,3,2,3,1]
n=len(num)
result=occurrences(num,n)
print(f"{result}")
