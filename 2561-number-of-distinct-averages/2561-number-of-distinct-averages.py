class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums=sorted(nums)
        left=0
        right=len(nums)-1
        seen=set()
        while left<right:
            mini=nums[left]
            maxi=nums[right]
            if (mini+maxi)/2 not in seen:
                seen.add((mini+maxi)/2)
            left+=1
            right-=1
        return len(seen)

