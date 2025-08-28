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
print(vow_swap("zoho corporation"))       # output : zohi carporotoon  '''

