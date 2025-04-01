class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d={}
        nums.sort()
        l=0
        r=len(nums)-1
        while l<r:
            if -nums[l]==nums[r]:
                return nums[r]
            
            elif -nums[l]>nums[r]:
                l+=1
            
            else:
                r-=1
        return -1

        