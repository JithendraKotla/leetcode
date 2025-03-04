class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        d={}
        nums=nums1+nums2

        for i in nums:
            id=i[0]
            num=i[1]
            if id in d:
                d[id]+=num
            else:
                d[id]=num
        new_num = [[i, j] for i, j in sorted(d.items())]
        
        return new_num