class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        def f(i,j):
            if i<0 or j<0:
                return 0
            
            if obstacleGrid[i][j]==1:
                return 0
            
            if i==0 and j==0:
                return 1

            if dp[i][j]!=-1:
                return dp[i][j]
            

            up=f(i-1,j)
            left=f(i,j-1)

            dp[i][j]=up+left
            return dp[i][j]
        dp=[[-1 for _ in range(m)] for _ in range(n)]

        return  f(n-1,m-1)
        