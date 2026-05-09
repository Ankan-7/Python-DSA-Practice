#Using Two Variable
l=[]
rear=-1
front=0
ms=20
def Enqueue(item):
    global rear
    if rear==ms-1:
        print("Queue is full")
    else:
        rear+=1
        l.append(item)
def Dequeue():
    global front
    global rear
    if front>rear:
        print("Queue is empty")
        rear=-1
        front=0
    else:
        t=l[front]
        print("the deleted element is",t)
        front+=1
def display():
    if len(l)==0:
        print("Queue is empty")
    else:
        print("Result =",l)

p=True
while p:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")
    p=int(input("Enter your choice:"))
    if p==1:
        x=int(input("Enter a number:"))
        Enqueue(x)
    elif p==2:
        Dequeue()
    elif p==3:
        display()
    elif p==4:
        p=False
    else:
        print("You enter wrong option...")

#Using One Variable
"""
l=[]
fr=-1
ms=20
def Enqueue(item):
    global fr
    if fr==ms-1:
        print("Queue is full")
    else:
        fr+=1
        l.append(item)
def Dequeue():
    global fr
    if fr==-1:
        print("Queue is empty")
    else:
        t=l.pop(0)
        print("the deleted element is",t)
        fr-=1
def display():
    if len(l)==0:
        print("Queue is empty")
    else:
        print("Result =",l)

p=True
while p:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")
    p=int(input("Enter your choice:"))
    if p==1:
        x=int(input("Enter a number:"))
        Enqueue(x)
    elif p==2:
        Dequeue()
    elif p==3:
        display()
    elif p==4:
        p=False
    else:
        print("You enter wrong option...")
"""