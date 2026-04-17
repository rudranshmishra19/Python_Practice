stack =[]

push=stack.append(1)
push=stack.append(12)
push=stack.append(4)
push=stack.append(33)

remove=stack.pop()



peepk=stack[-1]
print(peepk)

isEmpty= not bool(stack)
print(isEmpty)

isfull=bool(stack)
print(isfull)

# size 
print("size :",len(stack))

print(stack)