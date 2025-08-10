class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for price in prices:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash  