def anagram(a,b):
    if len(a)!=len(b):
        return False
    freq={}
    for c in a:
        freq[c]=freq.get(c,0)+1
    for c in b:
        if c not in freq or freq[c]==0:
            return False
        freq[c]-=1
    return True

print(anagram("listen","silent"))
    