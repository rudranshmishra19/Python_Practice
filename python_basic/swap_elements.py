arr=[10,20,30,40,50]
# Swap index 1 and index 2
# arr[1],arr[2]=arr[2],arr[1]
# print(arr)

# Using temp
# arr=[10,20,30,40,50]
# temp=arr[1]
# arr[1]=arr[2]
# arr[2]=temp
# print(arr)

# User input se swap
i=int(input("First index: "))
j=int(input("Second input: "))
arr[i],arr[j]=arr[j],arr[i]
print("After swap",arr)
