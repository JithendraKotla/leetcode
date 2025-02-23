class Solution(object):
    import heapq
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap=[]
        
        for i in stones:
            heapq.heappush(heap,-i)

        while heap:
            s1=-(heapq.heappop(heap))

            if not heap:
                return s1
            
            s2=-(heapq.heappop(heap))

            if s1>s2:
                heapq.heappush(heap,s2-s1)
        return 0




        

        
