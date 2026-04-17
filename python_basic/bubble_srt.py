
def bubble_srt(arr):
    length=len(arr)
    for i in range(length):
        for j in range(0,length-i-1):
          if arr[j]>arr[j+1]:
            #   manual way like C programming 
            #   temp=arr[j]
            #   arr[j]=arr[j+1]
            #   arr[j+1]=temp
            #  pythonic way 
              arr[j],arr[j+1]= arr[j+1],arr[j]

arr=[18,5,6,1,9]
print("Before sorting",arr)
bubble_srt(arr)
print("After sorting :",arr)



        
    
    
         