class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        c=0
        cost=sorted(cost,reverse=True)
        for i in range(0,len(cost),3):
            if i==len(cost)-1:
                c+=cost[i]
            else:
                c+=(cost[i]+cost[i+1])
        return c
        