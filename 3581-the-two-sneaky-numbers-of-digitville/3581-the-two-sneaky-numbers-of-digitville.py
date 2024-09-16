class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        res=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j ==2:
                res.append(i)
        return res
        