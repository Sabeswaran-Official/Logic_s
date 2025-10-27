'''1.pattern prb ;  output : 1
                             6 2
                             10 7 3
                             13 11 8 4
                             15 14 12 9 5  
n=5
m=n+1
r_num=1
for i in range(1,m):  
    col_num=r_num
    s=m-i
    for j in range(1,i+1):
        print(col_num,end=" ")
        col_num=col_num-s
        s+=1
    r_num=r_num+(m-i)
    
    print()  

# 2.find common in both arrays  ;input:arr1=[1,2,4,6,7,9] ,arr2=[2,3,4,5,8,9] ; output :2,4,9
def sol(a1,a2):
    result=[]
    for i in a1:
        cur=i
        for j in range(len(a2)):
            if a2[j]==cur:
                result.append(a2[j])
    return result

arr1=[1,2,4,6,7,9] 
arr2=[2,3,4,5,7,8,6,9]
print(sol(arr1,arr2))

# 3. Given 2 strings the 2nd str is present in 1st string in reverse ;return its index value
# str1="I came by car" ; str2="emac" output :2 -the str2 present in str1 aat 2nd in reverse order
str1="I was came by car"
str2="emac"
def sol(a1,a2):
    ss=a1.split(" ")
    print(ss)
    ind=0
    for i in range(0,len(ss)):
        re=ss[i][::-1]
        if re==a2:
            ind+=i+1
            return ind
print(sol(str1,str2))

# 4.convert numerical into words
# with in-build function
from num2words import num2words
print(num2words(235))
print(num2words(1978,lang="fr"))   #in french
print(num2words(1678935,to='currency',lang='es'))     #in spanish                 
# without in-build function

def num2word(num):
    
    if num==0:
        return "Zero"
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    def twoDigit(n):
        if n<20:
            return ones[n]
        else:
            return tens[n//10]+("" if n%10==0 else " "+ones[n%10])
        
    def threeDigit(n):
        hundred=n//100
        remainder=n%100
        # if hundred==0:
        #     return twoDigit(remainder)
        if remainder==0:
            return ones[hundred]+" hunderd"
        else:
            return ones[hundred]+ " hunderd and "+twoDigit(remainder)
        
    if num<100:
        return twoDigit(num)
    elif num<1000:
        return threeDigit(num)
    elif num<10000:
        thousand=num//1000
        remainder=num%1000
        if remainder==0:
            return ones[thousand]+" thousand"
        else:
            return ones[thousand]+" thousand and "+threeDigit(remainder)
    else:
        return "Number out of range"
             
print(num2word(219))
'''
# 5) given an expression, find whether duplicate bracket are present  ;Eg's : ((x+y)) - true ,  (x+y) - false ,  ((x+y)+((z))) - true ,  ((x+y)+(y+z)) - false

def solution(str):
    stack=[]
    for i in str:
        if i==")":
            if not stack:    #check stackk is empty
                return False
            if stack[-1]=="(":
                return True
            while stack and stack[-1]!="(":
                stack.pop()
            if stack:         #check stackk is not empty
                stack.pop()

        else:
            stack.append(i)
    return False

print(solution("((x+y))"))   