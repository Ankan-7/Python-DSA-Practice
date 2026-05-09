l=[]
def rear(item):
    l.append(item)
def front():
    return l.pop(0)
x=int(input("Enter a number:"))
while x>0:
    rear(x%10)
    x=x//10
s=0
while len(l)!=0:
    s=s*10 + front()
print(s)