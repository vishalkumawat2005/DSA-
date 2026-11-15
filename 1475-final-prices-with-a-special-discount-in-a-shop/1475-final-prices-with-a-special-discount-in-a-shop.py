class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack=[]
        ans=prices.copy()
        for i in range(len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                idx=stack.pop()
                ans[idx]-=prices[i]
            stack.append(i)
        return ans


