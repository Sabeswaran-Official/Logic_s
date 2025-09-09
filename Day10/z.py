# Segregate even & odd n a alternative position  input : [1,2,4,3,5,7,8,6]  ouput : [1,8,3,6,5,4,7,2]  -don't use external array.Do it in-place

class EvenOdd:
    def solution(arr):
        arr.sort(key=lambda x:(x%2==0 ,-x if x%2==0 else x))
        
        result=[]
        odd_end=0
 
        result=[]
        for i in range(len(arr)):
            if arr[i]%2!=0:
                odd_end+=1
        odd_ind,even_ind=0,odd_end
        while odd_ind<odd_end or even_ind<len(arr):
            if odd_ind<odd_end:
                result.append(arr[odd_ind]);odd_ind+=1
                
            if even_ind<len(arr):
                result.append(arr[even_ind])
                even_ind+=1
        
        return f"{arr} == {result}"
sol=EvenOdd
print(sol.solution([1,2,4,3,5,7,8,6,9]))
