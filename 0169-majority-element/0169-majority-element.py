class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
       
        max_key = max(d, key=d.get)


        max_value = d[max_key]
        return max_key