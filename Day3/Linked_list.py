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

    def insert_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_position(self,position,data):
        if position==0:
            self.insert_begining(data)
            return
        
        new_node=Node(data)
        current=self.head
        count=0

        while current and count<position-1:
            current=current.next
            count+=1

        if current is None:
            print("Position out of bounds")
            return
        
        new_node.next=current.next
        current.next=new_node

    def delete_by_value(self,target):
        if self.head is None:
            print("List is empty")
            return
        elif self.head==target:
            self.head=self.head.next
            return
        
        current=self.head
        while current.next and current.next.data !=target:
            current=current.next
        if current.next is None:
            print("value is not found in the list")
            return
        else:
            current.next=current.next.next

    def delete_by_position(self,position):
        if self.head is None:
            print("List is empty")
            return
        elif position==0:
            self.head=self.head.next
            return
        
        current=self.head
        count=0
        while current and count<position-1:
            current=current.next
            count+=1

        if current.next is None:
            print("position out of bounds")
        else:
            current.next=current.next.next


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
Dl.insert_begining(4)

Dl.print_forward()
Dl.print_backward()
Dl.delete_by_value(2)
Dl.print_forward()
Dl.delete_by_position(2)
Dl.print_forward()