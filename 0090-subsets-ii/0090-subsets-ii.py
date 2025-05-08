class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        n=len(nums)
        nums.sort()
        for i in range(1<<n):
            sub=[]
            for j in range(n):
                if (i&(1<<j)):
                    sub.append(nums[j])
            if sub not in res:
                res.append(sub)
       
        return res
        