from collections import defaultdict
count=defaultdict(int)

words=["apple","banana","apple","orange","banana","apple"]

for word in words:
    count[word]+=1
print(count)    