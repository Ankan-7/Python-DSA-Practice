l=[]
top=-1
ms=20
def Push(item):
    global top
    if top==ms:
        print("stack is full")
    else:
        top+=1
        l.append(item)
def Pop():
    global top
    if top==-1:
        print("Stack is empty")
    else:
        t=l.pop()
        print("the deleted element is",t)
        top-=1
def display():
    if len(l)==0:
        print("Stack is empty")
    else:
        print("Result =",l)

p=True
while p:
    print("1.push")
    print("2.pop")
    print("3.display")
    print("4.exit")
    p=int(input("Enter your choice:"))
    if p==1:
        x=int(input("Enter a number:"))
        Push(x)
    elif p==2:
        Pop()
    elif p==3:
        display()
    elif p==4:
        p=False
    else:
        print("You enter wrong option...")