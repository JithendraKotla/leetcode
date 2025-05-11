class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        tot = 0

        for i in range(m):
            for j in range(n):
                tot += grid[i][j]

   
        hori = 0
        for i in range(m - 1):  
            hori += sum(grid[i])
            if 2 * hori == tot:
                return True

       
        transposed = [[grid[i][j] for i in range(m)] for j in range(n)]

        veri = 0
        for i in range(n - 1):  
            veri += sum(transposed[i])
            if 2 * veri == tot:
                return True

        return False
