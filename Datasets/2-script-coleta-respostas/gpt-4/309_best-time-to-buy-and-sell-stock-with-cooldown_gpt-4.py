class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        sell, buy, cooldown = 0, -prices[0], 0
        
        for price in prices:
            sell, buy, cooldown = max(sell, buy + price), max(buy, cooldown - price), sell
            
        return sell