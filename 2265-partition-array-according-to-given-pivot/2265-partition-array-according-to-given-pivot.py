class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        piv=[]
        l_piv=[]
        r_piv=[]
        for i in nums:
            if i==pivot:
                piv.append(i)
            elif i<pivot:
                l_piv.append(i)
            else:
                r_piv.append(i)
        
        return l_piv+piv+r_piv
            
        

        