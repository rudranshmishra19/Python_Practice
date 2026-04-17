class Treenode:
    def __init__(self,left,right,value):
       self.left=None
       self.right=None
       self.value=value

def inorder_traversal(root):
    stack=[]
    current=root  #Start with root node

    while current or stack:
        #step 1 go as left as possible 
        while current:
            stack.append(current)
            current=current.left
        
        # Step 2 current is now none pop from the stack
        current=stack.pop()
        print(current.val,end=" ")

        #step 3:Move to right subtree
        current=current.right

#Build a sample tree:
root=Treenode(1)
root.left=Treenode(2)
root.right=Treenode(3)
root.left.left=Treenode(4)
root.left.right=Treenode(5)

# Call function
print("Inorder traversal(iterative)")
inorder_traversal(root)