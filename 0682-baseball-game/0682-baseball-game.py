class Solution(object):
    def calPoints(self, op):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack=[]
        

        for i in range(len(op)):
            if op[i]=="+":
                res=stack[-1]+stack[-2]
                stack.append(res)
                
            
            elif op[i]=="D":
                res=stack[-1]*2
                stack.append(res)
                
            
            elif op[i]=="C":
                stack.pop()

            else:
                stack.append(int(op[i]))
        return sum(stack)


        