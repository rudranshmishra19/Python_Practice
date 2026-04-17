# names=["Alice","Bob","Charlie"]
# ages=[25,30,35]

# for name,age in zip(names,ages):
#     print(f"{name} is {age} year old")

# # Different length list
# list1=[1,2,3,4]
# list2=['a','b']
# zipped=list(zip(list1,list2))
# print(zipped)

# Unzipping
# pairs=[(1,'a'),(2,'b'),(3,'c')]
# nums,letters=zip(*pairs)
# print(nums)  #(1,2,3)
# print(letters) #('a','b,'c)

left_shoes = ['🥿', '🥿', '👟']
right_shoes = ['🥿', '👟', '👟']

pairs = list(zip(left_shoes, right_shoes))
print(pairs)
