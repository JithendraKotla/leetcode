class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res=[]

        for i in range(len(A)):
            k=A[:i+1]
            c=0
            for j in k:
                if j in B[:i+1]:
                    c+=1
            res.append(c)
        return res
           
            
        