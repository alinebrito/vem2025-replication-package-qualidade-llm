class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices:
            return 0
        if k >= len(prices) // 2:
            return sum(max(0, b - a) for a, b in zip(prices, prices[1:]))

        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], buy[i] + price)

        return sell[k]