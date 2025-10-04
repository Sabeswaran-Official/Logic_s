# Sept -18 questions
'''
# 1.sum of two integers without + or -
def solution(a,b):
    while b!=0:
        mask=0xF        #for 4 bit  ;8-bit =0xFF ;32-bit : 0xFFFFFFFF
        mask_int=0x7    #for 4 bit  ;8-bit =0x7F ;32-bit : 0x7FFFFFFF
        carry=(a&b) & mask
        a=a^b & mask
        b=(carry<<1) & mask
    return a if a<=mask_int else ~(a^mask)
print(solution(-5,2))

# No.of ways to reach n steps     ;f(n)=f(n-1)+f(n-2)  ;f(1)=1 & f(2)=2
def solution(n):
    if n<=2 :
        return n
    else:
        pre2,pre1=1,2
        for i in range(3,n+1):
            cur=pre1+pre2
            pre2=pre1
            pre1=cur
        return cur
print(solution(5))
'''
# volume of water trapped in a 2-d height map
  


