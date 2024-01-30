class Solution:
   def evalRPN(self, tokens: List[str]) -> int:
        stack = []   
        for i in tokens:
            if i=="+":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(a+b))
            elif i=="-":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b-a))
            elif i=="*":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(a*b))
            elif i=="/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack.pop()



        