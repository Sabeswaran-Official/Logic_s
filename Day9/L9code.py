'''
# 394. Decode string
class decStr:
    def solution(string):
        stack=[]
        cur_str=""
        cur_num=0
        for char in string:
            if char.isdigit():
                cur_num=cur_num*10+int(char)
            elif char=="[":
                stack.append((cur_str,cur_num))
                cur_num=0
                cur_str=""
            elif char=="]":
                pre_str,num=stack.pop()
                cur_str=pre_str+cur_str*num
            else:
                cur_str+=char
        return cur_str

            
de=decStr
print(de.solution("3[a2[c]]"))


# Beauty flowers
def solution(flowers):
    n=len(flowers)
    min_height=min(flowers)
    max_height=max(flowers)
    beauty=max_height-min_height
    if max_height==min_height:
        ways=n*(n-1)/n
    else:
        ways=flowers.count(min_height)*flowers.count(max_height)

    return beauty,ways
print(solution([2,2,8,2,4,4,6,2,6,8]))

'''
# 54. Spiral matrix

class spiralMatrix:
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
sm=spiralMatrix
print(sm.solution([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))

