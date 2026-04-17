# sentene="I am a backend developer in google "
# words=sentene.split()
# word_length=[]
# for word in words:                             #common way
#     if word!="in":
#       word_length.append(len(word))
# print(words)
# print(word_length)      

#list comprehension to simplfy the process

sentence="I am ex-apple software engineer"
words=sentence.split()
word_length=[len(word)for word in words if word !="ex-apple"]
print(words)
print(word_length)

