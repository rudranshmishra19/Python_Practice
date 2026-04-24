# s="mama"
# half=len(s)//2
# # what is meant by symettry,if first half matches that second half ignoring the middle character
# sys= s[:half] == s[half:] if len(s)%2==0 else s[:half] == s[half+1:]
# pal = s ==s[::-1]
# print("Symmetrical" if sys else "Not Symmetrical")
# print("Palindrome" if pal else "Not palindrome")
# Two pointer techniques
def is_pal_is_sym(s):
    l,r=0,len(s)-1
    pal = True
    while l<r:
        if s[l]!=s[r]:
            pal=False
            break
        l+=1
        r-=1
    m=len(s)//2
    sym= True
    for i in range(m):
        if len(s)%2==0:
            if s[i]!=s[i+m]:
                sym=False
                break
        else:
            if s[i] !=s[i+m+1]:
                sym=False
                break

    return pal,sym      
s=input("enter a string:" )
print((is_pal_is_sym(s)))



