word=(input("Enter a word:")).replace(" "," ").lower()
reversed=word[: : -1]
if word==reversed:
    print(f"The {word} is palindrome")
else:
    print(f"The {word} is not a palindrome") 