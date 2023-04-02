############################
#QUEUE USING LINKLIST
############################
class Node:
    def __init__(self, n):
        self.data = n
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def insert(self, n):
        new_node = Node(n)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def delete(self):
        if self.front is None:
            return None
        else:
            temp = self.front
            self.front = self.front.next
            return temp.data
    def printlist(self):
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.delete()
q.printlist()
#######################
#STACK USING LINKLIST
#######################
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None 
class Stack:
    def __init__ (self):
        self.head = None
    def push(self, data):
        new_node =Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data
    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
s = Stack()
s.push(35)
s.push(69)
s.push(92)
s.push(100)
s.pop()
s.pop()
s.printlist()






























