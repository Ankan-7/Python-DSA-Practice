l=[]
def rear(item):
    l.append(item)
def front():
    return l.pop(0)
def str_palin(a):
    p =len(a)
    for i in range(p-1,-1,-1):
         rear(a[i])
    s=''
    while len(l)!=0:
         s=s+front()
    if a == s:
         return "Palindrome"
    else:
         return "Not Palindrome"
a=input("Enter the String :")
print(str_palin(a))