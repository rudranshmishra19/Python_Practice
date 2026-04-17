class TreeNode(object):
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution(object):
    def binaryTreePaths(self,root):

        paths=[]

        def dfs(node,path):
            if not node:
                return
            # Add current node value to path
            if path=="":
                path=str(node.val)
            else:
                path+="->"+str(node.val)

            # if leaf, append path
            if not node.left and not node.right:
                paths.append(path)
                return
            
            dfs(node.left,path)
            dfs(node.right,path)
        dfs(root,"")
        return paths   

a=TreeNode("1")
b=TreeNode("2")
c=TreeNode("3")
d=TreeNode("5")
a.left=b 
a.right=c
c.right=d
sol=Solution()
print(sol.binaryTreePaths(a))