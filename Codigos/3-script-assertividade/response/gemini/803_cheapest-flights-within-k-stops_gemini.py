class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            new_prices = prices.copy()
            for start, end, price in flights:
                if prices[start] != float('inf') and prices[start] + price < new_prices[end]:
                    new_prices[end] = prices[start] + price
            prices = new_prices

        return prices[dst] if prices[dst] != float('inf') else -1