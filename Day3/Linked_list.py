'''Types:  
    Singly linked list ,
    Doubly linked list ,
    Circular linked list ,
    Doubly circular linked list 

# Singly LinkedList
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return

        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
'''

# Doubly LinkedList
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        
        current=self.head
        while current.next:
            current=current.next

        current.next=new_node
        new_node.prev=current

    def print_forward(self):
        current=self.head

        while current:
            print(current.data,end="->")
            current=current.next
            last=current
        print("None")

    def print_backward(self):
        current=self.head
        if not current:
            print("Empty node")
            return

        current=self.head

        while current.next:
            current=current.next
    
        while current:
            print(current.data,end="<-")
            current=current.prev
        print("None")

Dl=DoublyLinkedList()
Dl.append(2)
Dl.append(3)
Dl.append("T")

Dl.print_forward()
Dl.print_backward()