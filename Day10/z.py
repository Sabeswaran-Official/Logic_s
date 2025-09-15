
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


# 165.Compare version numbers
class VersNo:
    def solution(version1,version2):
        ver1=list(map(int,version1.split(".")))
        ver2=list(map(int,version2.split(".")))
        max_length=max(len(ver1),len(ver2))
        ver1.extend([0]*(max_length-len(ver1)))
        ver2.extend([0]* (max_length-len(ver2)))
        
        for i in range(max_length):
            if ver1[i]<ver2[i]:
                return -1
            elif ver1[i]>ver2[i]:
                return 1
        return 0

vn=VersNo
print(vn.solution("1.0","1.0.0.0"))


# 44.Wildcard matching
def wildCardMatching(s,p):
    i,j=0,0
    start_ind=-1
    match=0

    while i<len(s):
        if j<len(p) and (p[j]==s[i] or p[j]=="?"):
            i+=1;j+=1
        elif j<len(p) and p[j]=="*":
            start_ind=j
            match=i
            j+=1
        elif start_ind!=-1:
            j=start_ind+1
            match+=1
            i=match
        else:
            return False

    while j<len(p) and p[j]=="*":
        j+=1

    return j==len(p)
print(wildCardMatching( "cb","?a"))


# Arange wave no's I/P   - [20, 40, 30, 50, 70, 80]  , O/P - [20, 40, 30, 70, 50, 80]    . Explanation :  a1 <= a2 >= a3 <= a4 >= a5....
def solution(arr):
    i=0
    j=1
    n=len(arr)

    while j<n:
        if i%2==0:
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                
        else:
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
        i+=1;j+=1
    return arr
print(solution([20, 40, 30, 50, 70, 80]))


# String -1st occurance ;integer -last occurance
str="abc23c4d32"
def solution(str):
    result=[]
    last_occ = {}
    for i, ch in enumerate(str):
        if ch.isdigit():
            last_occ[ch] = i

    seen_alpha=set()
    for i,ch in enumerate(str):
        if ch.isalpha():
            if ch not in seen_alpha:
                result.append(ch)
                seen_alpha.add(ch)

        else:
            if i==last_occ[ch]:
                result.append(ch)

    return "".join(result)
print(solution(str))
