# 
def valid_parenthes(s):
    map={"(":")","{":"}","[":"]"}
    stack=[]
    for char in s:
        print(char)
        if char in map:
            stack.append(char)
        else:    
    
             if not stack:
                 return False
             if map[stack.pop()]!=char:
                 return False
    return not stack
       
s="{}"
print(valid_parenthes(s))