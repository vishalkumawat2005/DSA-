class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        ans=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    row=0
                    col=0
                    for x in range(len(mat[0])):
                        row+=mat[i][x]
                    for x in range(len(mat)):
                        col+=mat[x][j]
                    if row==1 and col==1:
                        ans+=1
        return ans