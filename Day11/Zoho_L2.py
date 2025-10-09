# Sept-12 questions
'''
# 1.Spiral matrix   - input:[[1,2,3],[4,5,6],[7,8,9]]  ;output: [123698745] 
def solution(matrix):
    m=len(matrix)
    n=len(matrix[0])
    top,bottom=0,m-1
    left,right=0,n-1
    result=[]

    while top<=bottom and left<=right:
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1

        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right-=1

        if top<=bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left+=1
    return result
print(solution([[1,2,3],[4,5,6],[7,8,9]]))   
'''
''' 2.pattern printing   -  output:     1
                                      4 3 2
                                    9 8 7 6 5
                                16 15 14 13 12 11 10
                                16 15 14 13 12 11 10
                                    9 8 7 6 5
                                      4 3 2
                                        1            
def solution(n):
    m=n//2
    space=n+1

    for i in range(1,m+1):
        num=i**2
        col_count=i*2
    
        print(" "*space,end="")
        for j in range(1,col_count):
            print(num,end=" ")
            num-=1
        print()
        
        if i<3:
            space-=2
        if i==3:
            space=0
            x=m-4
            space=space+(3*x)
        if i>3:
            space-=3
    # space=0
    # for i in range(m,0,-1):
    #     num=i**2
    #     col_count=i*2
        
    #     print(" "*space,end="")
    #     for j in range(1,col_count):
    #         print(num,end=" ")
    #         num-=1
    #     print()
    #     if i>m-3:
    #         space+=3
    #     print(i,space)
    #     if i==m-3:
    #         space=n
    #     if i<m-3:
    #         space+=2

solution(8)   

#3. decimal to binary number
# with in-built function
def deci_Binary(n):
    result=[]
    num=n
    res=bin(num)[2:]  #without[2:] it display with 0b -it respresent the binary value
    return res
print(deci_Binary(28))  
# without in-built func
def solution(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    binary=""
    while num>0:
        remainder=num%2
        binary=str(remainder)+binary
        num=num//2
    return binary
print(solution(28))

#4. Max heights view only
def solution(arr):
    result=[]
    
    for i in arr:
        if len(result)==0:
            result.append(i)
        elif i >result[-1]:
            result.append(i)
    return result
print(solution([6,3,7,4,8,11,13]))

#5. Second max frequent number
def solution(arr):
    values=[]
    for i in arr:
        if i not in values:
            values.append(i)
    
    result=[]
    for i in range(len(values)):
        count=0
        for j in range(len(arr)):
            if values[i]==arr[j]:
                count+=1
        if count==2:
            result.append(values[i])
        
    return result
            
print(solution([1,3,2,1,2,4,1,2,3,4]))
'''
# 6.String segmentation badesd on dictionary of strings
# {"I","like","Sam","sung","samsung","man","go","mango"}  ;input:"Ilike","IlikeSamsung" ,output:: I like ,I like Samsung

def solution(s, wordDict):
    memo = {}

    def backtrack(start):
        # If we reached the end successfully
        if start == len(s):
            return []

        # If result already computed
        if start in memo:
            return memo[start]

        # Try the longest word first by going backwards from end
        for end in range(len(s), start, -1):
            word = s[start:end]
            if word in wordDict:
                res = backtrack(end)
                if res is not None:
                    memo[start] = [word] + res
                    return memo[start]

        memo[start] = None
        return None

    result = backtrack(0)
    if result is None:
        return None
    return " ".join(result)


print(solution("IlikeSamsung", {"I", "like", "Samsung","Sam", "sung", "man", "go", "mango"}))

        
 