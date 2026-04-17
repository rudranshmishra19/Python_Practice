def bubble_srt(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            print(f"i={i},j={j}, comparing {arr[j]} and {arr[j+1]}")
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return  arr

arr=[2,5,6,7,1]
print(bubble_srt(arr))
