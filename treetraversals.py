class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
    def height(self,root):
        if root==None:
            return 0
        lheight=self.height(root.left)
        rheight=self.height(root.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1
    
    def levelorder(self,root):
        if root==None:
            return []
        l=[root]
        res=[]
        while len(l):
            s=len(l)
            a=[]

            for i in range(s):
                root=l[0]
                l.pop(0)
                if root.left!=None:
                    l.append(root.left)
                if root.right!=None:
                    l.append(root.right)
                a.append(root.val)
            res.append(a)
        return res
        
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
print("Height of the Tree",root.height(root))
levelordl=[]
levelordl=root.levelorder(root)
print("Levelorder Traversal",levelordl)


