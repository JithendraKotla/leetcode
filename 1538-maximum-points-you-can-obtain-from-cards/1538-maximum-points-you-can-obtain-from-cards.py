class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftsum=0
        rightsum=0
        maxsum=0
        n=len(cardPoints)-1
        for i in range(k):
            leftsum+=cardPoints[i]
        rightindex=n
        maxsum=leftsum
        
        for i in range(k-1,-1,-1):
            leftsum-=cardPoints[i]
            rightsum+=cardPoints[rightindex]
            rightindex-=1
            maxsum=max(maxsum,leftsum+rightsum)
        return maxsum
        

