class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)==1:
            return False
        elif s[0]==")" or  s[0]=="]" or s[0]=="}":
            return False
        else:
            for i in range(len(s)):
                if s[i]=="(" or s[i]=="[" or s[i]=="{":
                    stack.append(s[i])
                elif s[i]==")" and "(" in stack:
                    if stack[-1]=="(":
                        stack.pop()
                elif s[i]=="]" and "[" in stack:
                    if stack[-1]=="[":
                        stack.pop()
                elif s[i]=="}" and "{" in stack:
                    if stack[-1]=="{":
                        stack.pop()
                else:
                    return False
        if stack != []:
            return False
        else:
            return True
                
