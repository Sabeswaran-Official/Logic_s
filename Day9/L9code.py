# 394. Decode string
class decStr:
    def solution(string):
        stack=[]
        cur_str=""
        cur_num=0
        for char in string:
            if char.isdigit():
                cur_num=cur_num*10+int(char)
            elif char=="[":
                stack.append((cur_str,cur_num))
                cur_num=0
                cur_str=""
            elif char=="]":
                pre_str,num=stack.pop()
                cur_str=pre_str+cur_str*num
            else:
                cur_str+=char
        return cur_str

            
de=decStr
print(de.solution("3[a2[c]]"))
