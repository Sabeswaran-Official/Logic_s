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
'''
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

