class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        concat=0
        while l<r:
            sum=int(str(nums[l])+str(nums[r]))
            concat+=sum
            l+=1
            r-=1
        if l==r:
            concat+=nums[l]
        return concat
