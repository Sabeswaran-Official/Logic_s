# 14-sep 2025 questions
#1. regex finding 1st occurance   ;
'''input :  str=chcabbac, regex :cab*ac   ;output : cabbac
notes:  a* ->a can occur 0 or more times ,a+ ->a can occur 1 or moretimes ;a ->a can occur atleast one time 

def solution(str,regex):
    i=0
    pattern=""
    while i<len(regex):
        if regex[i]=="*":
            prev=regex[i-1]
            j=str.find(pattern)
            if j!=-1:
                while j+len(pattern)<len(str) and str[j+len(pattern)]==prev:
                    pattern+=prev
            i+=1
        if regex[i]=="+":
            prev=regex[i-1]
            j=str.find(pattern)
            if j!=-1:
                count=0
                while j+len(pattern)<len(str) and str[j+len(pattern)]==prev:
                    pattern+=prev
                    count+=1
                if count==0:
                    return None
            i+=1
        else:
            pattern+=regex[i]
            i+=1

    if pattern in str:
        return pattern
    else:
        return None

print(solution("chcabbac","cab+ac"))   

#2. Sort odd no.s in descending order & even no.s in ascending order  ;input - 1 5 2 6 4 6 3  ,output : 5 3 2 4 6 6 1
def solution(arr):
    odd_nos=sorted([x for x in arr if x%2!=0],reverse=True)
    even_nos=sorted([x for x in arr if x%2==0])
    
    result=[]
    odd_ind,even_ind=0,0
    for num in arr:
        if num%2!=0:
            result.append(odd_nos[odd_ind])
            odd_ind+=1
        elif num%2==0:
            result.append(even_nos[even_ind])
            even_ind+=1
    return result
print(solution([1,5,2,6,4,6,3,7,9,8]))
'''
#3. sum based on frequency ,input:12341  ,output: 1-->9 ,2-->2         ?????
def solution(arr):
    freq={}
    for ch in arr:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    result=[]
    for i ,j in freq.items():
        print(ke)
                
solution([1,2,3,4,1])  
'''
# 4.Sort in wave form
def solution(arr):
    i=0
    while i<len(arr)-1:
        if i%2==0:
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        else:
            if arr[i]<arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]

        i+=1
    return arr

print(solution([10,24,34,64,27,23,8]))

# remove duplicates in a string ;   condition  :  keep the 1st occurance of alphabets * last occurance of numbers
def solution(str):
    result=[]
    last_occ={}
    for i,ch in enumerate(str):
        if ch.isdigit():
            last_occ[ch]=i
    
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

print(solution("abca12cf3124"))

# comparing version numbers 
def solution(version1,version2):
    ver1=list(map(int,version1.split(".")))
    ver2=list(map(int,version2.split(".")))
    max_length=max(len(ver1),len(ver2))
    ver1.extend([0]*(max_length-len(ver1)))
    ver2.extend([0]*(max_length-len(ver2)))

    for i in range(max_length):
        if ver1[i]<ver2[i]:
            return -1
        elif ver1[i]>ver2[i]:
            return 1
    return 0

print(solution("2.0.5","2.1.0.0"))
'''