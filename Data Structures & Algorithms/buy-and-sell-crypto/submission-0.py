class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, b = 0, 1, 0

        for i in range(1, len(prices)):
            if prices[i] > prices[l]:
                b = max(prices[i] - prices[l], b)
            else:
                l = i
        return b