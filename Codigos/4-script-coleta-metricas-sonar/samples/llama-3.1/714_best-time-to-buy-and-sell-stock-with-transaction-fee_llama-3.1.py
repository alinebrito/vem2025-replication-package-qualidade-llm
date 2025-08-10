class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = -prices[0], 0
        for price in prices[1:]:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
        return sell