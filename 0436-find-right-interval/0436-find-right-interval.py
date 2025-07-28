class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        starts=[[i[0],j] for j,i in enumerate(intervals)]
        starts.sort()
        res=[]
        for interval in intervals:
            low=0
            high=len(starts)-1
            end=interval[1]
            idx=-1
            while low<=high:
                mid=(low+high)//2
                if starts[mid][0]>=end:
                    high=mid-1
                    idx=starts[mid][1]
                else:
                    low=mid+1
            res.append(idx)
        return res

        