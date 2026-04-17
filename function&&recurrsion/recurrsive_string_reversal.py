def reversal(s):
    #base case: if string is empty or 1 char,it is already reversed 
    if len(s)<=1:
      return s
    # Recursive case:reverse the rest of the string and append the first char
    return reversal(s[1:])+s[0]

#Example usage
name="Rudransh"
reverse=reversal(name)


