'''
n=4
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()

Output :   1
          121
         12321
        1234321     

n=4
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    for j in range(i-1,0,-1):
        print("*",end="")
    print()

Outpt :    *
          ***
         *****
        *******  

n=4
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    for j in range(i-1,0,-1):
        print("*",end="")
    print()

Output : *******
          *****
           ***
            *             

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

output :    1
            12
            123
            1234   
n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

output: 54321
        4321
        321
        21
        1    

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

# Diamond pattern
def solution(n):
    
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for j in range(1,i+1):
            print("*",end="")
        for j in range(i-1,0,-1):
            print("*",end="")
        print()
    for i in range(n-1,0,-1):
        print(" "*(n-i),end="")
        for j in range(1,i+1):
            print("*",end="")
        for j in range(i-1,0,-1):
            print("*",end="")
        print()

print(solution(4))

n=8
m=int(n/2)
num=1
for i in range(1,m):
    count=2*i-1
    temp=[]
    for i in range(count):
        temp.append(num)
        num+=1
    temp_r=temp[::-1]
    print(" "*(m*2-i)+" ".join(str(x)for x in temp_r))

for i in range(m//2):
    num=n+2
    temp=[]
    for i in range(n-1):
        temp.append(num)
        num+=1
    temp_r=temp[::-1]
    print(" ".join(str(x) for x in temp_r))
for i in range(m-1,0,-1):
    count=2*i-1
    temp=[]
    num=n-i
    
    for i in range(count):
        temp.append(num)
        num+=1
    
    temp_r=temp[::-1]
    num=temp_r[-1]//2

    print(" "*(n-i)+" ".join(str(x)for x in temp_r))

'''
n = 6   # number of rows in the top half
num = 1

# Top half
rows = []
for i in range(1, n ):
    count = 2 * i - 1
    temp = [num + j for j in range(count)]
    num += count
    row = " " * (n+1 - i) *2 + " ".join(str(x) for x in reversed(temp))
    rows.append(row)
    print(row)
print(temp)
# num_1=int(rows[2][6])
# for i in range(n-2):
#     for j in range(n*n,num_1+1,-1):
#         print(j,end=" ")
#     print()
# rev_row=rows[::-1]
# for i in rev_row:
#     print(i)



