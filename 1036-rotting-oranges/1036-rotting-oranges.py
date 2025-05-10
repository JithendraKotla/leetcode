class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0]) 
        fresh=0
        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        if fresh==0:
            return 0
        t=-1

        while q:
            len_q=len(q)
            t+=1
            for _ in range(len_q):
                i,j = q.popleft()
                for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=r<m and 0<=c<n  and grid[r][c]==1 :
                        grid[r][c]=2
                        fresh-=1
                        q.append((r,c))
        if fresh==0:
            return t
        return -1