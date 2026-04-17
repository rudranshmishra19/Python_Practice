elements=[1,2,1,4,5,2,4,1]
frequency={}
for  item in elements:
     if item in frequency:
        frequency[item]+=1
     else:
         frequency[item]=1

print(frequency)