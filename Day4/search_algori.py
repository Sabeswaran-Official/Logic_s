# LinearSearch  &  BinarySearch


def lin_sea(arr,target):
    n=len(arr)
    global t 
    t=target
    for i in range(n):
        if arr[i]==target:
            return i
            
    return -1
result=lin_sea([1,2,3,4,5,6],3)

if result==-1:
    print(f"The value {t} is not found in the list")
else:
    print(f"The value {t} is found in the index of {result} ")      

# Binary search
def bina_sea(arr,target):
    global t
    t=target
    n=len(arr)
    mid=n//2
    low=arr[0]
    high=arr[n-1]
    for i in range(n):
        if arr[i]==target:
            return i
        elif target<arr[mid]:
            high=arr[mid-1]
        elif target>arr[mid]:
            low=arr[mid+1]
    return -1
result=bina_sea([1,2,3,4,5],6)

if result==-1:
    print(f"The value {t} is not found in the list")
else:
    print(f"The value {t} is found in the index of {result} ") 