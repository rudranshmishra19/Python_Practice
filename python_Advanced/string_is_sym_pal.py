# # Given a string check if it is Symmetrical or Palindrome
# s="amaama"
# half=len(s)//2
# sym=s[:half] == s[half:] if len(s)%2==0 else s[:half] == s[half+1:]
# pal = s == s[:: -1]

# print("Symmetrical" if sym else "Not Symmetrical")
# print("Palindrome" if pal else "Not palindrome")

# palindrome if amaama = is amaama 
# Two pointer
def is_sym_is_pal(s):
    pal=True
    l,r=0,len(s)-1
    while l<r:
        if s[l]!=s[r]:
            pal =False
            break
        l+=1
        r-=1
    half=len(s)//2
    sym=True
    for i in range(half):
        if len(s)%2==0:
            if s[i]!=s[i+half]:
                sym=False
                break
            if s[i]!=s[i+half+1]:
                sym=False
                break
    return pal,sym

   
s=input("Enter a string:"  )
print(is_sym_is_pal(s))




# amamma = ammama
#amamma = ama = mma
