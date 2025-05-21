class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mini=float('inf')
        ans=-1
        c=0

        for i,j in points:
            if i==x or j==y:
                dist=abs(i-x)+abs(j-y)
                if dist<mini:
                    mini=dist
                    ans=c
            c+=1
        return ans
            

        
        
        