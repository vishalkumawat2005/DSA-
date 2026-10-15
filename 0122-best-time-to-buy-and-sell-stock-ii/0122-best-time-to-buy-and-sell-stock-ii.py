class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy=float('inf')
        profit=0
        for price in prices:
            buy=min(buy,price)
            profit=max(profit,profit+price-buy)
            buy=price
        return profit
        