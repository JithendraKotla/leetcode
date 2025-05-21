class Solution:
    def customSortString(self, order: str, s: str) -> str:
        notinorder=""
        for i in s:
            if  i not in order:
                notinorder+=i
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        inorder=""
        for i in order:
            if i in s:
                inorder+=i*d[i]
        
        return inorder+notinorder

        