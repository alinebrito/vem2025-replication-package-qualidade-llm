class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        
        n = len(prices)
        if k > n // 2:
            return sum(max(0, prices[i] - prices[i-1]) for i in range(1, n))
        
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)
        
        for i in range(n):
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j-1] - prices[i])
                sell[j] = max(sell[j], buy[j] + prices[i])
        
        return sell[k]