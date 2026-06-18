arr=[1,2,3,4]
arr1=[2,40]
try:
    for i in arr:
       if arr[i] not in arr1:
          arr1.append(arr[i])
except  IndexError:
   print("An indexError happened,but we caught it")
print(arr1)    

