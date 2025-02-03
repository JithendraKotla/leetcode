class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dec=1
        inc=1
        a=0
        if n==1:
            return 1
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                dec+=1
                inc=1
            elif nums[i-1]<nums[i]:
                inc+=1
                dec=1
            else:
                inc=dec=1
            a=max(a,inc,dec)
        return a
        