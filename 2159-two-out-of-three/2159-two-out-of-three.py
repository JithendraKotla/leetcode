class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        d={}

        nums1=list(set(nums1))
        nums2=list(set(nums2)) 
        nums3=list(set(nums3))

        num=nums1+nums2+nums3

        for i in num:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res=[]
        for i,j in d.items():
            if j>=2:
                res.append(i)
        
        return res


