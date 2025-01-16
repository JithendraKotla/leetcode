class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n1=len(nums1)
        n2=len(nums2)
        xor1=0
        xor2=0

        if n1%2:
            for i in nums2:
                xor2^=i
        if n2%2:
            for i in nums1:
                xor1^=i
        return xor1^xor2


        