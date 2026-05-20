class Node:
    def __init__(self,data):
        self.data,self.next=data,None
class single_linked_list:
    def __init__(self):
        self.head=None
    def create(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    
    def display(self):
        c=self.head
        while c:
            print(c.data,end="->")
            c=c.next
        print("None")
l=single_linked_list()
"""l.create(10)
l.create(20)
l.create(30)
l.display()"""
p=True
while p:
    print("1. Create")
    print("2. Display")
    print("3. Exit")
    r=int(input("Enter your Choice :"))
    if r==1:
        n=int(input("Enter Number:"))
        l.create(n)
    elif r==2:
        l.display()
    elif r==3:
        p=False
    else:
        print("Wrong Option..")