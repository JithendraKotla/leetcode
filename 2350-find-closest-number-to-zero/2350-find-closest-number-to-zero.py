class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min=abs(nums[0]-0)
        a=nums[0]
        for i in nums:
            if abs(i-0)<min:
                min=abs(i-0)
                a=i
        if a<0:
            if -a in nums:

                return -a
        return a