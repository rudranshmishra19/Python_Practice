text="A man, a plan, a canal:Panama"
lowercase_text=text.lower()
res=''.join(char for char in text if char.isalnum()).lower()
if res == res[::-1]:
    print("Text is palindrome")
else:
    print("Text is not a palindrome")


