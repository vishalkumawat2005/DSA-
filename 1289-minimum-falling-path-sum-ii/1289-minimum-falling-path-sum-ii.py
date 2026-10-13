
class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)

        for i in range(1, n):
            for j in range(n):
                mini = float('inf')

                for k in range(n):
                    if k != j:
                        mini = min(mini, grid[i - 1][k])

                grid[i][j] += mini

        return min(grid[n - 1])

