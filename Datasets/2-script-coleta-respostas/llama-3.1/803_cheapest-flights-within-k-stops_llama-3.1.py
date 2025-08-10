class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, price in flights:
            graph[u].append((v, price))
        
        import heapq
        min_heap = [(0, src, 0)]
        while min_heap:
            price, city, stops = heapq.heappop(min_heap)
            if city == dst:
                return price
            if stops <= k:
                for neighbor, cost in graph[city]:
                    heapq.heappush(min_heap, (price + cost, neighbor, stops + 1))
        return -1