class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                arr = nums[i:j+1]

                if prod(arr) == lcm(*arr) * gcd(*arr):
                    res = max(res, len(arr))

        return res