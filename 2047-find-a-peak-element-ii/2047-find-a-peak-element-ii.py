class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def findMaxIndex(mat,n,m,col):
            maxVal=-1
            index=-1
            for i in range(0,n):
                if maxVal< mat[i][col]:
                    maxVal=mat[i][col]
                    index=i
            return index
        n=len(mat)
        m=len(mat[0])

        low=0
        high=m-1
        while low<=high:
            mid=(low+high)//2
            maxRowIndex=findMaxIndex(mat,n,m,mid)

            if mid-1>0:
                left=mat[maxRowIndex][mid-1]
            else:
                left=-1
            
            if mid+1<m:
                right=mat[maxRowIndex][mid+1]
            else:
                right=-1
            if mat[maxRowIndex][mid]>left and mat[maxRowIndex][mid]>right:
                return [maxRowIndex,mid]
            elif mat[maxRowIndex][mid]<left:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]