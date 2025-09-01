'''# Ques : input : hello ;output: holle          
def vow_swap(s):
    
    s_list=list(s)
    vowels=set("aeiouAEIOU")
    i,j=0,len(s_list)-1

    while i<j:
        while i<j and s_list[i] not in vowels:
            i+=1
        while i<j and s_list[j] not in vowels:
            j-=1

        if i<j:
            s_list[i],s_list[j]=s_list[j],s_list[i]
            i+=1
            j-=1
    return "".join(s_list)
print(vow_swap("zoho corporation"))       # output : zohi carporotoon 

n=5
for i in range(1,n+1,+1):
    print(" "*(n-i),end="")
    for j in range(i,i*2,+1):
        print(j,end="")
    for j in range(2*i-2,i-1,-1):
        print(j,end="")  
    print()
    output :
              1
             232
            34543
           4567654
          567898765      

arr=[1,1,1,1,1,2,2,2,3,3,4,4,4,4,5,5]
n=len(arr)

result=[]
for i in set(arr):    
    count=0
    for j in range(0,n):
        if arr[j]==i:
            count+=1 
    result.append(f"{i}-->{count}")
print(",".join(result))

output :  1-->5,2-->3,3-->2,4-->4,5-->2   '''