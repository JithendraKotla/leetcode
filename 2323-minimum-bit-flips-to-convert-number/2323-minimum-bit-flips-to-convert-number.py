class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        c=0
        startb=bin(start)[2:]
        goalb=bin(goal)[2:]
        maxi=max(len(startb),len(goalb))
        startb=startb.zfill(maxi)
        goalb=goalb.zfill(maxi)
        for i in range(len(startb)):
            
            if startb[i]!=goalb[i]:
                c+=1
        return c