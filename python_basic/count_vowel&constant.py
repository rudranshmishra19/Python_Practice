str="A queit lazy dog jumps on the fox"
vowels="AEIOUaeiou"

for ch in str:

    if ch.isalpha():
        if ch in vowels:

         print(f"{ch} is vowel")
        else:
         print(f"{ch} is consonant")       

    
