class Solution:
    def canCross(self, stones: list[int]) -> bool:
        n = len(stones)
        stone_set = set(stones)
        dp = {}
        def solve(pos, jump):
            if pos == stones[-1]:
                return True

            if (pos, jump) in dp:
                return dp[(pos, jump)]

            for k in (jump - 1, jump, jump + 1):
                if k > 0 and pos + k in stone_set:
                    if solve(pos + k, k):
                        dp[(pos, jump)] = True
                        return True

            dp[(pos, jump)] = False
            return False

        return solve(0, 0)