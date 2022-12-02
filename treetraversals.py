class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
    def preorder(self,root,l):
        if root:
            l.append(root.val)
            self.preorder(root.left,l)
            self.preorder(root.right,l)
    def postorder(self,root,l):
        if root:
            self.postorder(root.left,l)
            self.postorder(root.right,l)
            l.append(root.val)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
inordl=[]
root.inorder(root,inordl)
preordl=[]
root.preorder(root,preordl)
postordl=[]
root.postorder(root,postordl)
print("Inorder Traversal",inordl)
print("PreOrder Traversal",preordl)
print("Postorder Traversal",postordl)

