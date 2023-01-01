class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        result=int(tokens[0])
        for i in tokens:
            if(i!="+" and i!="-" and i!="*" and i!="/"):
                stack.append(int(i))
            else:
                if(i=="+"):
                    a=stack.pop()
                    b=stack.pop()
                    result=b+a
                    stack.append(result)
                elif(i=="-"):
                    a=stack.pop()
                    b=stack.pop()
                    result=b-a
                    stack.append(result)
                elif(i=="*"):
                    a=stack.pop()
                    b=stack.pop()
                    result=b*a
                    stack.append(result)
                elif(i=="/"):
                    a=stack.pop()
                    b=stack.pop()
                    result=int(b/a)
                    stack.append(result)
        return(result)
