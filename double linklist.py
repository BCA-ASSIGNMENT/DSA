######################################################
#IMPLEMENTATION OF DOUBLE LINKED LIST IN PYTHON
######################################################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.last = None
    def createlist(self,n):
        newnode=Node(n)
        if self.head is None:
            self.head=newnode
            self.last=newnode
        else:
            newnode.prev=self.last
            self.last.next=newnode
            self.last=newnode
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
        while self.last is not None:
            print(self.last.data)
            self.last=self.last.prev
l=DoubleLinkList()
l.createlist(1)
l.createlist(2)
l.createlist(3)
l.createlist(4)
l.printlist()
