# 73. Set matrix zeros

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

'''
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



        ***   Generator Expression   ***
all(x > 0 for x in nums) → checks if all numbers are positive.
any(word == "hello" for word in words) → checks if "hello" exists in the list.   '''

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