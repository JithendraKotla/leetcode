class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float("inf")
        left=0
        cur=0
        for right in range(len(nums)):
            cur+=nums[right]
            while cur>=target:
                mini=min(mini,right-left+1)
                cur-=nums[left]
                left+=1
        if mini==float("inf"):
            return 0
        return mini
