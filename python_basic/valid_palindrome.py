s="bac"
l,r=0,len(s)-1
b=True
while l<r:
    if s[l]!=s[r]:
        b=False
        break
    l+=1
    r-=1
print(b)

