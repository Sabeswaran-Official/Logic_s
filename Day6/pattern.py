'''n=4
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
Output :   *
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
            *             '''