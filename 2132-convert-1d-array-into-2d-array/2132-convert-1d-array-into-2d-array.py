class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original)!=m*n:
            return []
        
        else:
            res=[]
            for i in range(0,len(original),n):
                res.append(original[i:i+n])
            return res
        