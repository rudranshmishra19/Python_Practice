nums=[1,1,2,2,3,3,3,4]
freq={}
k=3
for n in nums:
    freq[n]=freq.get(n,0)+1

sorted_list=sorted(freq.items(),key=lambda x:x[1], reverse=True)
result=[key for key ,value in sorted_list[:k]]
print(sorted_list)
print(result)