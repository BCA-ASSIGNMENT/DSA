class List:
    def __init__(self, n):
        self.data = n
        self.address = None
class LinkList:
    def __init__(self):
        self.head = None
        self.last = None
    def createList(self, n):
        newnode = List(n)
        if self.head is None:
            self.head = newnode
        else:
            self.last.address = newnode
        self.last = newnode
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.address
    def insert_at_front(self, n):
        newnode = List(n)
        newnode.address = self.head
        self.head = newnode
    def insert_at_end(self, n):
        newnode = List(n)
        if self.head is None:
            self.head = newnode
        else:
            self.last.address = newnode
        self.last = newnode
    def insert_at_pos(self, n, pos):
        newnode = List(n)
        temp = self.head
        for i in range(pos-1):
            temp = temp.address
        newnode.address = temp.address
        temp.address = newnode
    def delete_at_front(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.address
            return temp.data
    def delete_at_end(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            while temp.address.address is not None:
                temp = temp.address
            temp.address = None
    def delete_at_pos(self, pos):
        if self.head is None:
            return None
        else:
            temp = self.head
            for i in range(pos-1):
                temp = temp.address
            temp.address = temp.address.address
k=LinkList()
k.createList(5)
k.createList(6)
k.insert_at_front(40)
k.insert_at_end(50)
k.insert_at_pos(60,2)
k.delete_at_front()
k.delete_at_end()
k.delete_at_pos(2)
k.printList()
