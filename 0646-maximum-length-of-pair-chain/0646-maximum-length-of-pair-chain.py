class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        res=1
        pairs.sort(key = lambda x:x[1])

        start=pairs[0][1]
        n=len(pairs)

        for i in range(1,n):
            if pairs[i][0]>start:
                res+=1
                start=pairs[i][1]
        return res