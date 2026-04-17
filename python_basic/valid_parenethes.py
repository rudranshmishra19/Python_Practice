def isValid(s:str)->bool:
    stack=[]
    mapping={')':'(','}':'{',']':'['}
 
    for char in s:
    # if it's a closing bracket
      if char in mapping:
        #  pop the top of the stack if not empty,else assign dummy value
         top_element=stack.pop() if stack else '#'

        # Check if the mapping matches
         if mapping[char]!=top_element:
            print(mapping[char])
            return False
      else:
        #  it is an opening bracket->push onto stack
          stack.append(char)
    # if stack is empty, all brackets matched 
    return not stack
    

# Example usage 
# True
print(isValid("()")) 
