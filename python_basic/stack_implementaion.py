class stack:
    def __init__(self):
       self.stack=[]

    def push(self,elemnet):
        self.stack.append(elemnet)

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return"Stack is Empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
#Create a stack 
myStack=stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack :",myStack.stack)
print("pop :",myStack.pop())
print("peek :",myStack.peek())
print("isEmpty:",myStack.isEmpty())
print("Size:",myStack.size())

