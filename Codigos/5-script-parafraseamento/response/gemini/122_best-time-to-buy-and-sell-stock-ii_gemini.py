class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2: 
          return 0
        
        current_min = float('inf')
        max_profit = 0

        for i in prices:
          if i < current_min:
            current_min = i
          if i - current_min > max_profit:
            max_profit = i - current_min
        
        return max_profit  