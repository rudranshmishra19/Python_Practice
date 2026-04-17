def is_symmetrical(s):
    # Using two pointer techniques
    pal=True
    left,right=0,len(s)-1
    while left<right:
        if s[left]!=s[right]:
            pal=False
            break
        left+=1
        right-=1
      
    # Symmmetry check (first half == second half)
    # Odd-length strings cant be symmettical
    sym=False
    if len(s)%2==0:
        half=len(s)//2
        sym=True
        for i in range(half):
            if s[i]!=s[i+half]:
                sym =False
                break
    return sym,pal   

    



s=input("Enter a string: ")
print(is_symmetrical(s))
