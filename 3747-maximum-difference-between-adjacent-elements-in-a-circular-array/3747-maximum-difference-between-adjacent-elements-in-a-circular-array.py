class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxi=float("-inf")
        for i in range(1,len(nums)):
            diff=abs(nums[i]-nums[i-1])
            maxi=max(diff,maxi)
        maxi=max(maxi,abs(nums[-1]-nums[0]))
        return maxi
        