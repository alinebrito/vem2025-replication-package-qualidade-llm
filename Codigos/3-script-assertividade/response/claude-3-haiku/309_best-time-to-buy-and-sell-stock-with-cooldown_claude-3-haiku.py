class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        n = len(prices)
        buy = -prices[0]
        sell = 0
        prev_sell = 0
        
        for i in range(1, n):
            temp = sell
            sell = max(sell, buy + prices[i])
            buy = max(buy, prev_sell - prices[i])
            prev_sell = temp
        
        return sell