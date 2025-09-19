# Sept -18 questions

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


