
n=4
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
'''
Output :   1
          121
         12321
        1234321     '''

n=4
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    for j in range(i-1,0,-1):
        print("*",end="")
    print()
'''
Output :   *
          ***
         *****
        *******  '''

n=4
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    for j in range(i-1,0,-1):
        print("*",end="")
    print()
'''
Output : *******
          *****
           ***
            *             '''

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''
output :    1
            12
            123
            1234   '''
n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
'''
output: 54321
        4321
        321
        21
        1    '''

n=5
for i in range(1,n+1,+1):
    print(" "*(n-i),end="")
    for j in range(i,i*2,+1):
        print(j,end="")
    for j in range(2*i-2,i-1,-1):
        print(j,end="")  
    print()   
    '''
output :
              1
             232
            34543
           4567654
          567898765   '''
    
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


def diamondPattern(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for j in range(1,i*2):
            print("*",end="")
        print()
    for i in range(n-1,0,-1):
        print(" "*(n-i),end="")
        for j in range(1,i*2):
            print("*",end="")
        print()

print(diamondPattern(4))



