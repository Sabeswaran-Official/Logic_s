from collections import deque
from queue import LifoQueue

stack=deque()
arr=[]
stack.append(1)
stack.append(2)
arr.append(3)
arr.append(4)
print(stack)
print(arr)
stack.pop()
arr.pop()
print(stack)
print(arr)
sta=LifoQueue()
stac=Queue()
stac.put(7)
stac.put(8)
sta.put(9)
sta.put(0)
print(stac.get())
print(sta.get())
print(sta.qsize())
print(sta)

# Reverse a str
def reverse_str(str):
    str1=deque(str)
    reverse=''
    while str1:
        reverse+= str1.popleft()
    return reverse
print(reverse_str("olleh"))

def is_balancing(str):
    stack=deque()
    pairs= {"A":"a","B":"b","C":"c"}
    for i in str:
        if i in 'ABC':
            stack.append(i)
        elif i in 'abc':
            if not stack or stack.pop() != pairs [i]:
                return False
    return stack

print(is_balancing("ABCabc"))

# ????
def postfix(str):
    stack=deque()
    
    for i in str.split():
        if i.isdigit():
            stack.append(int(i))
        else:
            b=stack.pop()
            a=stack.pop()
            if i =="+":
                stack.append(a+b)
            elif i =="-":
                stack.append(a-b)
            elif i =="*":
                stack.append(a*b)
            elif i =="%":
                stack.append(a%b)
            elif i =="/":
                stack.append(a/b)
    return stack

print(postfix("2 3 1 + 9 -")) 
