#BINARY SEARCH TREE IN PYTHON
class node:
    def __init__(self, n):
        self.data = n
        self.lson=None
        self.rson=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self, n):
        newnode=node(n)
        if self.root==None:
            self.root=newnode
        else:
            temp=self.root
            while temp != None:
                prev=temp
                if n<temp.data:
                    temp=temp.lson
                else:
                    temp=temp.rson
            if n<prev.data:
                prev.lson=newnode
            else:
                prev.rson=newnode
    def inorder(self, root):
        if root != None:
            self.inorder(root.lson)
            print(root.data)
            self.inorder(root.rson)
    def preorder(self, root):
        if root != None:
            print(root.data)
            self.preorder(root.lson)
    def postorder(self, root):
        if root.lson != None:
            self.postorder(root.lson)
        if root.rson != None:
            self.postorder(root.rson)
            print(root.data)
t=bst()
t.insert(5)
t.insert(3)
t.insert(7)
t.insert(2)
t.insert(4)
t.insert(6)
t.insert(8)
t.inorder(t.root)
t.preorder(t.root)
t.postorder(t.root)
