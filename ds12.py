s=[]
def push():
    if len(s)==size:
        print("Stack is full")
    else:
        item=input("Enter the element:")
        s.append(item)
def pop():
    if (len(s)==0):
        print("Stack is empty")
    else:
        item=s[-1]
        del(s[-1])
        print("the deleted element is:",item)
def display():
    size=len(s)
    if(size==0):
        print("Stack is empty")
    else:
        for i in reversed(s):
            print(i)
size=int(input("Enter the size of the stack:"))
while(True):
    choice=int(input("1-push 2-pop 3-display 4-exit Enter your choice:"))
    if (choice==1):
        push()
    elif (choice==2):
        pop()
    elif (choice==3):
        display()
    else:
        break
    
