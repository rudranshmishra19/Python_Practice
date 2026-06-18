s=["flower","flow","floor"]
# print(s[0],s[1],s[2])
# sort the array first
# floor,flow,flower
ans=""
s=sorted(s)
first=s[0]
last=s[-1]
# print(first,last)
for i in range(min(len(first),len(last))):
    if (first[i]!=last[i]):
         break
    ans+=first[i]
print(ans)


