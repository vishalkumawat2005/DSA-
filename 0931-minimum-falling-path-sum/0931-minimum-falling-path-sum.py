class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        m=len(matrix)
        for i in range(1,m):
            for j in range(0,m): 
                top=matrix[i-1][j]
                left=matrix[i-1][j-1] if j>0 else float('inf')
                right=matrix[i-1][j+1] if j<m-1 else float('inf')
                matrix[i][j]+=min(top,left,right)
        return min(matrix[m-1])
