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
        #return t


p=input("Enter the String :")
a=len(p)
for i in range(a):
        Push(p[i])
s=''
while top!=-1:
    s=s+Pop()
if p==s:
     print("Palindrome")
else:
     print("Not Palindrome")