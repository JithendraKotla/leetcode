class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        for i in range(len(nums)-1):
            sum=nums[i]+nums[i+1]
            if sum in d:
                d[sum]+=1
            else:
                d[sum]=1
            if d[sum]>=2:
                return True
        return False