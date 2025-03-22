import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap=[]
        res=[]
        
        for i in range(len(nums)):
            heapq.heappush(heap,(-int(nums[i])))
        
        while k>0:
            res.append(heapq.heappop(heap))
            k-=1
        return str(res[-1]*-1)



        