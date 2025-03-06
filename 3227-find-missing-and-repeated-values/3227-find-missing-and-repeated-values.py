class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n=len(grid)
        arr=[i for i in range(1,n**2+1)]

        d={}
        flat=[]
        res=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                flat.append(grid[i][j])
                if grid[i][j] in d:
                    d[grid[i][j]]+=1
                else:
                    d[grid[i][j]]=1
        for i,j in d.items():
            if j==2:
                res.append(i)
        for i in arr:
            if i not in set(flat):
                res.append(i)
        return res
        


