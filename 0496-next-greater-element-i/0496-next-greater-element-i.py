class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[-1]*len(nums1)
        for i in range(len(nums1)):
            j=nums2.index(nums1[i])
            for k in range(j+1,len(nums2)):
                if nums2[k]>nums1[i]:
                    ans[i]=nums2[k]
                    break
        return ans
        