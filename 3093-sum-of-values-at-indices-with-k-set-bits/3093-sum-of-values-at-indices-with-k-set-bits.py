class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
       
        res=0
        for i in range(len(nums)):
            bin_num=bin(i)[2:]
            if bin_num.count("1")==k:
                res+=nums[i]
        return res
            
        