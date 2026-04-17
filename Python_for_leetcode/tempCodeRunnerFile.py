def anyalze_text(text):
    words=text.split()
    # Count frequency of each words
    freq={}
    for word in words:
         freq[word]=freq.get(word,0)+1

    #print frequency of each word
    print("Word frequency")
    for word,count in freq.items():
         print(f"{word}:{count}")

    #return freq
    return freq

text="A quick brown fox jumps over the lazy dog"
anyalze_text(text)          

