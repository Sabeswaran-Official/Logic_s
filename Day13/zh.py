# Sept -18 questions
'''
# 1.sum of two integers without + or -
def solution(a,b):
    while b!=0:
        mask=0xF        #for 4 bit  ;8-bit =0xFF ;32-bit : 0xFFFFFFFF
        mask_int=0x7    #for 4 bit  ;8-bit =0x7F ;32-bit : 0x7FFFFFFF
        carry=(a&b) & mask
        a=a^b & mask
        b=(carry<<1) & mask
        
    return a if a<=mask_int else ~(a^mask)
print(solution(5,-2))

# No.of ways to reach n steps     ;f(n)=f(n-1)+f(n-2)  ;f(1)=1 & f(2)=2
def solution(n):
    if n<=2 :
        return n
    else:
        pre2,pre1=1,2
        for i in range(3,n+1):
            cur=pre1+pre2
            pre2=pre1
            pre1=cur
        return cur
print(solution(8))   

 volume of water trapped in a 2-d height map
   Sample Test Cases:
 Input:
 4 8
 8 8 8 8 6 6 6 6
 8 0 0 8 6 0 0 6
 8 0 0 8 6 0 0 6
 8 8 8 8 6 6 6 0
 Output:
 56
 Input:
 3 3
 3 3 3
 3 1 3
 3 3 3
 Output:
 2
 Input:
 3 4
 1 4 3 1
 3 2 1 3
 2 3 3 2
 Output:
 4         
# Trapping Rain Water II - no heapq, no sorting, manual min-extraction
# Reads from stdin:
# First line: m n
# Next m lines: n integers each
# Prints single integer: total trapped water

def trap_rain_water_manual(heightMap):
    if not heightMap or not heightMap[0]:
        return 0

    m = len(heightMap)
    n = len(heightMap[0])

    # visited matrix
    visited = [[False for _ in range(n)] for _ in range(m)]

    # "queue" will hold entries [effective_height, r, c]
    # start with all boundary cells
    queue = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                queue.append([heightMap[i][j], i, j])
                visited[i][j] = True

    total_water = 0

    # 4-direction moves
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    # While queue not empty, manually extract minimum element
    while queue:
        # find index of minimum effective_height
        min_idx = 0
        min_val = queue[0][0]
        k = 1
        while k < len(queue):
            if queue[k][0] < min_val:
                min_val = queue[k][0]
                min_idx = k
            k += 1

        # pop the minimum entry
        entry = queue.pop(min_idx)
        cur_h = entry[0]
        r = entry[1]
        c = entry[2]

        # check neighbors
        di = 0
        while di < 4:
            dr = dirs[di][0]
            dc = dirs[di][1]
            nr = r + dr
            nc = c + dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                neigh_h = heightMap[nr][nc]
                if neigh_h < cur_h:
                    # water trapped here
                    total_water += (cur_h - neigh_h)
                    new_eff = cur_h
                else:
                    new_eff = neigh_h
                queue.append([new_eff, nr, nc])
            di += 1

    return total_water


# ---------------------------
# main: read input and run
# ---------------------------
def main():
    # read first line
    first = input().strip()
    while first == "":
        first = input().strip()
    parts = first.split()
    m = int(parts[0])
    n = int(parts[1])

    heightMap = []
    i = 0
    while i < m:
        line = input().strip()
        if line == "":
            continue
        row_parts = line.split()
        # allow rows possibly split across lines (defensive)
        row = []
        j = 0
        while j < n:
            row.append(int(row_parts[j]))
            j += 1
        heightMap.append(row)
        i += 1

    result = trap_rain_water_manual(heightMap)
    print(result)

if __name__ == "__main__":
    main()
                      
# Minimum cost to paint houses , Problem Statement: There are N houses in a row, and each house must be painted in one of three colors: red, green, or blue. The painting cost of each house with a certain color is provided in an N×3 matrix. The constraint is that no two adjacent houses can have the same color. Find the minimum
 total cost to paint all houses.
  Sample Test Cases:
 Input:               Input:                 Input :4
 3                     2                      3 2 7
 2 11 14                                      6 5 3
 11 5 13               5 7 8                  4 9 1
 14 15 7               9 4 6                  8 6 2
 Output:14            Output : 9             Output : 11

def solution(n,arr):
    prev_red=arr[0][0]
    prev_green=arr[0][1]
    prev_blue=arr[0][2]

    i=1
    while i<n:
        red=arr[i][0]+min(prev_green,prev_blue)
        green=arr[i][1]+min(prev_red,prev_blue)
        blue=arr[i][2]+min(prev_red,prev_green)

        prev_red,prev_green,prev_blue=red,green,blue
        i+=1
    res=min(prev_red,prev_green,prev_blue)
    return res
print(solution(4,[[9,4,6],[5,7,8],[8,6,2],[15,14,7]]))

# 24 card game ; Problem Statement: You are given 4 distinct integers between 1 and 9 (inclusive). Using all four
 numbers exactly once, and using any combination of '+', '-', '*', '/' and parentheses, determine if it is
 possible to make the value 24. Print true if possible, otherwise false.  Inp:4 1 8 7,outp:True ; inp:1234,out:True ; inp:1112 ,out:false

def solution(nums):
    if len(nums)<1:
        return None
    if len(nums)==1:
        if nums[0]==24:
            return True
        else:
            return False
        
    n=len(nums)
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            a=nums[i]
            b=nums[j]

            remaining=[]
            for k in range(n):
                if k!=i and k!=j:
                    remaining.append(nums[k])
            vals=[]
            vals.append(a+b)
            vals.append(a-b)
            vals.append(b-a)
            vals.append(a*b)
            if b!=0:
                vals.append(a/b)
            if a!=0:
                vals.append(b/a)

            for val in vals:
                final=[]
                for x in remaining:
                    final.append(x)
                final.append(val)
                if solution(final):
                    return True
    return False

print(solution([1,4,6,2]))
'''
# conway game's of life
