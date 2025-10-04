
# 73. Set matrix zeros  
'''
class Solution:
    def solve(self, matrix):
        m, n = len(matrix), len(matrix[0])

        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        
        return matrix

sol = Solution()
print(sol.solve([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))


class Solution:
    def solve(self,matrix):
        m=len(matrix)
        
        f=0
        l=m
        for i in range(m):
            n=len(matrix[i])
            if i==0 or i==n-1:
                for j in range(1,n-1):
                    matrix[i][j]=0
            else:
                matrix[i][0],matrix[i][n-1]=0,0
        return matrix
                
       
sol=Solution()
print(sol.solve([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))



        # ***   Generator Expression   ***
# all(x > 0 for x in nums) → checks if all numbers are positive.
# any(word == "hello" for word in words) → checks if "hello" exists in the list.   

class Solution:
    def setZeros(self,matrix):
        row=len(matrix)
        col=len(matrix[0])

        first_row=any(matrix[0][j]==0 for j in range(col))    #use this simple method or use if method seperatly to define which used below
        first_col=bool()
        for i in range(row):
            if matrix[i][0]==0:
                first_col=True

        print(first_row)
        print(first_col)

sol=Solution()
print(sol.setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))   


# 53.Maximum subarray

# basic solution which takes more time / time complexity & more calculations
def maxValue(arr):
    if not arr:
        return 0
    
    ans=arr[0]
    for i in range(len(arr)):
        cur_sum=0
        for j in range(i,len(arr)):
            cur_sum+=arr[j]
            ans=max(ans,cur_sum)
    return ans

print(maxValue([1]))

# also return the max subarray list with the max value
def maxValue(arr):
    if not arr:
        return 0
    
    ans=arr[0]
    best_start,best_end=0,0
    for i in range(len(arr)):
        cur_sum=0
        for j in range(i,len(arr)):
            cur_sum+=arr[j]
            if cur_sum>ans:
                ans=cur_sum
                best_start,best_end=i,j
     
    print(f"max subarray list : {arr[best_start:best_end+1]}")
    print(f"max value : {ans}")

maxValue([-2,1,-3,4,-1,2,1,-5,4])          

# Original solution ,which supports in leetcode
# float('-inf')    -- in pyhon it represents thenegative infinity ;    −∞ means "smaller than any real number."

class Solution:
    def maxvalue(self, nums) :
        ans=float('-inf')
        cur_val=0
        for num in nums:
            cur_val+=num
            if cur_val>ans:
                ans=cur_val
            if cur_val<0:
                cur_val=0
        return ans
sol=Solution()

print(sol.maxvalue([5,4,-1,7,8]))      


# maximum continous sub array

# .zfill(width) -- its a string method which just add zeros in a free space of left side;usefull in brute force(fixed length guesses)
for i in range(5):
    print(str(i).zfill(3),end=" ")      # output :  000 001 002 003 004 
'''
# 1668. Maximum Repeating Substring
class maxReapeat:
    def maxReapeatingSubstr(sequence,word):
        count = 0
        repeated = word
        while repeated in sequence:
            count += 1
            repeated += word
        return count
mm=maxReapeat
print(mm.maxReapeatingSubstr("cababab","a"))

# Solution below using re -regex expression  
import re
class maxReapeat:
    def maxReapeatingSubstr(sequence,word):
        matches=re.findall(word,sequence)
        count=len(matches)
        result="".join(matches)
        return f"{count} & the substring is {result}"
        


        # n=len(word)
        
        # ind=[]
        # end=[]
        # for match in re.finditer(word,sequence):
        #     ind.append(match.start())
        #     end.append(match.end())
        
        # x=ind[0]
        
        # if  count>1:
        #     print(f" {sequence[x:count*n+(n%2)+1]} is a substring of {sequence} ")   
        
        
mm=maxReapeat
print(mm.maxReapeatingSubstr("cabababa","a"))
