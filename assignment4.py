#############################
#IMPLEMENT OF STACK IN PYTHON
###############################
import numpy as np
stack=np.zeros(5,dtype='int16')
top=-1
def push(n):
    global top
    if top==4:
        print("overflow")
        return
    else:
        top=top+1
        stack[top]=n
def pop():
    global top
    if top==-1:
        print("underflow")
    else:
        print("deleted element is",stack[top])
        top=top-1
while True:
    ch=int(input("<1>insert<2>delete<3>exit"))
    if (ch==1):
        x=int(input("enter a value"))
        push(x)
    elif (ch==2):
        pop()
    elif (ch==3):
        break
#################
#OMPLEMENT OF QUEUE IN PYTHON
#################
import numpy as np
n=np.zeros(10,dtype=int)
rear=-1
front=0
def insert(n):
    global rear
    if rear==9:
        print("OVERFLOW")
    else:
        rear+=1
        n[rear]=int(input("ENTER THE ELEMENT : "))
def delete():
    global front
    if front>rear:
        print("UNDERFLOW")
    else:
        print("DELETED ELEMENT IS:",n[front])
        front=front+1
while True:
    ch =int(input("<1> INSERT <2> DELETE <3> EXIT: "))
    if ch==1:
        insert(n)
    elif ch==2:
        delete()
    elif ch==3:
        break
 ########################
#IMPLEMENT OF CIRCULER QUEUE
#############################
import numpy as np
front=0
rear=-1
queue=np.zeros(10,dtype='int16')
def insert(n):
    global rear
    if rear-front==9:
        print("overflow!!")
    else:
        rear=rear+1
        queue[rear%10]=n
        print("inserted element is:",queue[rear%10])
def pop():
    global front
    if front>rear:
        print("Underflow!")
    else:
        print("deleted element is:",queue[front%10])
        top=top+1
while True:
    ch=int(input("<1 push><2 pop><3 exit>"))
    if ch==1:
        x=int(input("enter an element: "))
        insert(x)
    elif ch==2:
        pop()
    elif ch==3:
        break

