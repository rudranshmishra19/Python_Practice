def word(name):
    result={} #start as an empty list
    for i,char in enumerate(name):
        result[i]=char
    return result
name_list=word("Rudransh")
print(name_list)
        