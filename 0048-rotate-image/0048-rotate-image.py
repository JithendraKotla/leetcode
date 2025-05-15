class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
        res=[]
        for i in transposed:
            res.append(i[::-1])
        
        for i in range(len(res)):
            for j in range(len(res[i])):
                matrix[i][j]=res[i][j]
        return matrix

        