class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        d1={}
        for i in target:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        d2={}
        for i in arr:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        return d2==d1
        