l=[]
top=-1
ms=20
def Push(item):
    global top
    if top==ms-1:
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
    
def bracket_dect(n):
    for i in n:
        if i=='(' or i=='[' or i=='{':
            Push(i)
        elif i==')' or i==']' or i=='}':
            if top!=-1:
                t=Pop()
                if i==')' and t=='(' or i==']' and t=='[' or i=='}' and t=='{':
                    x=print("Bracket Complete")
                    return x

n=input("Enter a String :")
print(bracket_dect(n))
