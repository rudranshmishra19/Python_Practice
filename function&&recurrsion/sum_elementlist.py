def sum_list(lst):
    if not lst: #base case :empty list
        return 0
    return lst[0] + sum_list(lst[1:])

lst=[1,5,7,6]
result=sum_list(lst)
print(result)