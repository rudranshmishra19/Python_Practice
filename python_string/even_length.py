#finding even length using list compherension
# s="This is me then who is that"
# word=s.split()
# even_words=[w for w in word if len(w)%2==0]
# res=" ".join(even_words)
# print(res)
# Using filter
# k="i got supplies"
# words=k.split()
# even_wrds=filter(lambda w:len(w)%2==0,words)
# res=" ".join(even_wrds)
# print(res)

# Using geneartor
# a="I feel it another version of me"
# wrds=a.split()
# even_wrds=(w for w in wrds if len(w)%2==0)
# res=" ".join(even_wrds)
# print(res)
# Using itertools.compress()
from itertools import compress
s= "Python is fun language"
words = s.split()
selectors=[len(w)%2==0 for w in words]
res=" ".join(compress(words,selectors))
print(res)
