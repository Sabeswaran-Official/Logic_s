# from queue import Queue
from collections import deque
# queue=Queue(maxsize=5)

def rev_que(p):
    
    if not p:
        return
    item=p.popleft()
    rev_que(p)
    p.append(item)

p=deque("the")
rev_que(p)
print(p) 

def is_palindrome(str):
    q=deque(str)
    while q:
        if q.popleft()!=q.pop():
            return False
        else:
            return True

str="man"
print(is_palindrome(str))  


# Queue using Two Stacks
class Stackqueue():
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def enqueue(self,item):
        self.stack1.append(item)
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        return None

sq=Stackqueue()
sq.enqueue("a")
sq.enqueue("b")
print(sq.dequeue())  

# Transaction Scheduler Simulation
import time
def transac_schedu(trans):
    que=deque(trans)
    while que:
        q=que.popleft()
        print(f"Processing:{q}")
        time.sleep(3)

transac_schedu(["transaction_1","transaction_2","transaction_3"])

# Binary no generator ;what is binary no? form using 1 & 0  ;Eg:13 (decimal) = 1101 (binary)
def Binary_no_gene(n):
    result=[]
    q=deque()
    q.append("1")
    for i in range(n):
        binary=q.popleft()
        result.append(binary)
        q.append(binary+"0")
        q.append(binary+"1")
    s=result.pop()
    print(f"The binary no of {n} is {s}")
Binary_no_gene(3)

