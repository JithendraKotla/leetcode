class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<=1:
            return "1"
        prev=self.countAndSay(n-1)
        count=1
        res=[]

        for i in range(1,len(prev)):

            if prev[i-1]==prev[i]:
                count+=1
            else:
                res.append(str(count)+prev[i-1])
                count=1
            
        res.append(str(count)+prev[-1])
        return ''.join(res)
       
            

        