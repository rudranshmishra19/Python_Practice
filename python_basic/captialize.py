def capitalize_sentence(sentence):
    words=[]
    for word in sentence.split():
        capitalized=word[0].upper()+word[1:].lower()
        words.append(capitalized)
    return " ".join(words)    


sentence="I am a backend developer"
capitalize_sentence(sentence)
print(capitalize_sentence(sentence))