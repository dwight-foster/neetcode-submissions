class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, p = prices[0], 0

        for price in prices:
            l = min(price, l)
            p = max(p, price - l)
        return p