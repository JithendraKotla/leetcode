class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini=float("inf")
        n=len(nums)
        for size in range(l,r+1):
            for i in range(n-size+1):
                sub=nums[i:i+size]
                if sum(sub)>0:
                    mini=min(sum(sub),mini)
        if mini==float("inf"):
            return -1
        return mini
        