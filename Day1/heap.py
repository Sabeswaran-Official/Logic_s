import heapq

arr=[12,3,4,5,44,87]
print(arr)
heapq.heapify(arr)
print(arr)
heapq.heappop(arr)
print(arr)

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

print(heap)  # Output: [1, 10, 5] 

nums=[8,3,1,6,4,7,2]
heapq.heapify(nums)
print(nums)   

nums=[21,77,45,12,89,2,46,84]
heapq.heapify(nums)
print(nums)   


# Priority Queue with heapq
import heapq

pq = []
# (priority, value)
heapq.heappush(pq, (2, "eat"))
heapq.heappush(pq, (4, "code"))
heapq.heappush(pq, (6, "sleep"))
heapq.heappush(pq, (1, "drink"))
heapq.heappush(pq, (3, "bath"))
heapq.heappush(pq, (7, "brush"))
heapq.heappush(pq, (5, "play"))
print(pq)
while pq:
    priority, task = heapq.heappop(pq)
    print(f"{task} (priority {priority})")