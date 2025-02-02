class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp=sorted(nums)

        for i in range(len(nums)):
            r=nums[i:]+nums[:i]
            if r==temp:
                return True
        return False

        