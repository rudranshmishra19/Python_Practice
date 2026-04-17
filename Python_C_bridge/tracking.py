# List of numbers(can be words or string too)
numbers=[1,2,3,2,4,1,5]
# Create a "used " array to track processed elements
used=[False]*len(numbers)
# Loop through the list 
for i in range(len(numbers)):
    if used[i]: #skip if already used
        continue

    current=numbers[i]
    print(f"Processing:{current}")


    # Mark all duplicates occurrences as used
    for j in range(i+1,len(numbers)):
        if numbers[j]==current:
            used[j]=True

