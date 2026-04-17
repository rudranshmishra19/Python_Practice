word=(input("Enter a word:")).replace("","").lower()
print(f"you entered {word}")

reversed =""
i=len(word)-1 #start form the last index

while i>=0:
    reversed+=word[i]
    i-=1

if word==reversed:
    print("It is palindrome")
else:
    print("It is not a palindrome")    
