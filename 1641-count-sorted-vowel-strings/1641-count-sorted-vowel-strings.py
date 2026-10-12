
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5

        for length in range(2, n + 1):
            for i in range(3, -1, -1):
                dp[i] += dp[i + 1]

        return sum(dp)
