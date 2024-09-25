class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_p=0
        min_p=float('inf')
        for i in prices:
            if i<min_p:
                min_p=i
            d=i-min_p
            if d>max_p:
                max_p=d
        return max_p
        