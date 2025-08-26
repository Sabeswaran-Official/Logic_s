# Ques : input : hello ;output: holle
arr="hello"
vowels=["a","e","i","o","u"]
f=0
l=0
f_val=""
l_val=""
arr1=arr.split()
for i in range(0,len(arr)):
    if arr[i] in vowels:
        f_val+=arr[i]
        f+=i
        print(f_val)
        print(f)
        break
for j in range(len(arr)-1,0,-1):
    if arr[j] in vowels:
        l_val+=arr[j]
        l+=(j-(len(arr)-1))
        print(l_val)
        print(l)
        break


    