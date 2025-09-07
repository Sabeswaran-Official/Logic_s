# Ques : input : hello ;output: holle          
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
#    output :
#             1
#            232
#           34543
#          4567654
#         567898765      

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

# output :  1-->5,2-->3,3-->2,4-->4,5-->2   

# Trapping rain water -using Two Pointer Approach--time_complexity-O(n) ,space_complexity -O(1)

def trapRainWater(height):
    water=0
    left=0
    right=len(height)-1
    left_max=right_max=0

    while left<right:
        if height[left]<height[right]:
            if height[left]>=left_max:
                left_max=height[left]
            else:
                water+= left_max-height[left]

            left+=1
        else:
            if height[right]>=right_max:
                right_max=height[right]
            else:
                water+=right_max-height[right]
            right-=1
        
    return water

print(trapRainWater([4,2,0,3,5]))

# Best time to buy & sell stock
prices=[7,2,1,6,3,8,4]
def buySellStock(prices):
    min_price=float('inf')
    max_profit=0
    print(min_price)

    for price in prices:
        min_price=min(min_price,price)
        profit=price-min_price
        max_profit=max(max_profit,profit)

    buyDay,sellDay=0,0
    for i in range(len(prices)):
        if prices[i]==min_price:
            buyDay=i+1
        elif prices[i]==max_profit:
            sellDay=i+1
    
    return f"Buy in Day{buyDay} & sell at Day{sellDay} to make more profit"
print(buySellStock(prices))