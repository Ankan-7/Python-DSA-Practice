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
        top-=1
        return t

p=int(input("Enter the number: "))
while p>=1:
    Push(p)
    p-=1
f=1
while top!=-1:
    f=f*Pop()
print(f)