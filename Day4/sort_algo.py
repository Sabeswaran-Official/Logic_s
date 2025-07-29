# Types :
# Bubble sort ,insertion sort ,selection sort ,merge sort ,quick sort ,built-in sorting -- .sort()
'''
def bubblesort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr=[2,4,1,7,3]
bubblesort(arr)
print(arr)

def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        min_ind=i
        for j in range(i+1,n):
            if arr[min_ind]>arr[j]:
                min_ind=j
        arr[i],arr[min_ind]=arr[min_ind],arr[i]
arr=[2,4,1,7,3]
selectionSort(arr)
print(arr)  

def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        
arr=[2,4,1,7,3]
insertionSort(arr)
print(arr)   

def  mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i=j=k=0

        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                arr[k]=left_half[i]
                i+=1
            else:
                arr[k]=right_half[j]
                j+=1
            k+=1
        while i<len(left_half):
            arr[k]=left_half[i]
            i+=1
            k+=1
        while j<len(right_half):
            arr[k]=right_half[j]
            j+=1
            k+=1
    else:
        return arr
arr=[2,4,1,7,3]
mergeSort(arr)
print(arr) 
'''
# Quicksort is a divide-and-conquer sorting algorithm. It's widely used because it's efficient for large datasets.Time-complexity :O(n log n)
def quickSort(arr):
    if len(arr)<=1:
        return arr
    
    pivot=arr[0]
    left=[x for x in arr[1:] if x<pivot]
    right=[x for x in arr[1:] if x>=pivot]
    return quickSort(left)+[pivot]+quickSort(right)

arr=[2,4,1,7,3]
result=quickSort(arr)
print(result) 
