def push():
    global top
    n = input("Enter a number: ")
    top = top+1
    stack[top] = n
    print("Overflow",stack)
def pop():
    global top
    if top == -1:
        print("Stack Underflow")
    else:
        e = stack[top]
        top =top- 1
        print("Underflow", e)
        print(stack)
import numpy as np
stack = np.zeros(5, dtype=int)
top = -1
while True:
    ch = int(input("<1> Push <2> Pop <3> Exit: "))
    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        break
