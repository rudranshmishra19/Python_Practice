def remove_duplicates(s):
    result=""
    for char in s:
        if char in result:
            continue
        result+=char
    return result       
s="rudransh"
print(remove_duplicates(s))