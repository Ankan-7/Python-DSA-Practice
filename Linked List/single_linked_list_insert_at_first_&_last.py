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
    def insert_at_first(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_at_last(self,data):
        new_node=Node(data)
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
    print("2. Insert at first")
    print("3. Insert at last")
    print("4. Display")
    print("5. Exit")
    r=int(input("Enter your Choice :"))
    if r==1:
        n=int(input("Enter Number:"))
        l.create(n)
    elif r==2:
        n=int(input("Enter a Number :"))
        l.insert_at_first(n)
    elif r==3:
        n=int(input("Enter a Number:"))
        l.insert_at_last(n)
    elif r==4:
        l.display()
    elif r==5:
        p=False
    else:
        print("Wrong Option..")