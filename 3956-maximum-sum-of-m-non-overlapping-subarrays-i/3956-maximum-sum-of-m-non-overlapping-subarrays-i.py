
from collections import deque
class Solution:
    def maximumSum(self, nums: list[int], m: int, l: int, r: int) -> int:
        n = len(nums)

        qerunavilo = (nums, m, l, r)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        NEG = float('-inf')
        prev = [0] * (n + 1)

        ans = NEG

        for k in range(1, m + 1):
            curr = [NEG] * (n + 1)
            dq = deque()

            for i in range(1, n + 1):
                j = i - l

                if j >= 0 and prev[j] != NEG:
                    value = prev[j] - prefix[j]

                    while dq and dq[-1][1] <= value:
                        dq.pop()

                    dq.append((j, value))

                while dq and dq[0][0] < i - r:
                    dq.popleft()

                curr[i] = curr[i - 1]

                if dq:
                    curr[i] = max(
                        curr[i],
                        prefix[i] + dq[0][1]
                    )

            ans = max(ans, curr[n])
            prev = curr

        return ans
