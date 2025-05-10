class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res=0
        a,b,c=sorted([a,b,c])
        while (a > 0 and b > 0) or (b > 0 and c > 0) or (c > 0 and a > 0):
            a,b,c=sorted([a,b,c])
            if (b > 0 and c > 0):
                b -= 1
                c -= 1
                res += 1
        return res
            

            
