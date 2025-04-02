class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        arr=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (i<j<k):
                        arr.append((nums[i]-nums[j])*nums[k])
        if not arr:
            return 0
        
       
        return max(max(arr), 0)