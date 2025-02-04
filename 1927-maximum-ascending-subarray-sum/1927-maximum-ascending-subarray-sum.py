class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=0
        for i in range(len(nums)):
            end=i+1
            cur=nums[i]
            while (end < len(nums) and nums[end]>nums[end-1]):
                cur+=nums[end]
                end+=1
            maxi=max(cur,maxi)
        return maxi
