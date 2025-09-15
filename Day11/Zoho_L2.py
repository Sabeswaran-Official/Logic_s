# Sept-12 questions
# 1.Spiral matrix   - input:[[1,2,3],[4,5,6],[7,8,9]]  ;output: [123698745] 
'''
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

# 2.pattern printing   -  output:       1
                                      4 3 2
                                    9 8 7 6 5
                                16 15 14 13 12 11 10
                                16 15 14 13 12 11 10
                                    9 8 7 6 5
                                      4 3 2
                                        1                      '''
def solution(n):


print(solution())

