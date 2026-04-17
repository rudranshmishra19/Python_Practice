def sort_words(words_list):
    s_sort={}
    for word in words_list:
        s_sort[word]=''.join(sorted(word))
    return s_sort
#Test with multiple words
result=sort_words(["Rudransh","jeet","omkar"])
print(result)
 