class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]

        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            else:
                max_profit = max(max_profit, price - buy_price)

        return max_profit