class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        z=0
        for i in  arr1:
            c=0
            for j in arr2:
                if abs(i-j)>d:
                    c+=1
            if c==len(arr2):
                z+=1

                    
        return z