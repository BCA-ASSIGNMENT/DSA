##################################################################
#IMPLEMENTATION FD DOUBLE LINK LIST IN PYTHON
##################################################################
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
    def delete_at_last(self):
        if self.head != None:
            self.last.prev.next = None
            self.last = self.last.prev
        else:
            print("list is empty")
    def insert_at_pos(self, n, pos):
        newnode = Node(n)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode
        newnode.prev = temp
        newnode.next.prev = newnode
    def delete_at_front(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data
l=DoubleLinkList()
l.createlist(1)
l.createlist(2)
l.createlist(3)
l.createlist(4)
l.insert_at_pos(8, 2)
l.delete_at_last()
l.delete_at_front()
l.printlist()
