class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def gcd_of_array(arr):
            result = arr[0]
            for num in arr[1:]:
                result = gcd(result, num)
            return result

        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        def lcm_of_array(arr):
            result = arr[0]
            for num in arr[1:]:
                result = lcm(result, num)
            return result

        def prod(arr):
            pro = 1
            for i in arr:
                pro *= i
            return pro

        res = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):  
                arr = nums[i:j + 1]
                if prod(arr) == lcm_of_array(arr) * gcd_of_array(arr):
                    res = max(res, len(arr))

        return res
