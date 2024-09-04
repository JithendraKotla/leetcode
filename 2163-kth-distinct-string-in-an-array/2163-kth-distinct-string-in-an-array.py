class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        arr_set=set(arr)
        arr_set_l=list(arr_set)
        res=[]
        for i in arr:
            if arr_set_l.count(i)==arr.count(i):
                res.append(i)
        if len(res)<k:
            return ""
        else:
            return res[k-1]
        