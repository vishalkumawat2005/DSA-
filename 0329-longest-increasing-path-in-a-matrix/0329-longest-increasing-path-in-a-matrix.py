
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            dp[i][j] = 1

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + di, j + dj

                if (0 <= x < m and 0 <= y < n
                        and matrix[x][y] > matrix[i][j]):
                    dp[i][j] = max(dp[i][j], 1 + dfs(x, y))

            return dp[i][j]

        ans = 0

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans
