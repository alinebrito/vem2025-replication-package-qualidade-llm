class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [[float('inf')] * (k + 2) for _ in range(n)]
        dp[src][0] = 0
        for i in range(1, k + 2):
            for u, v, w in flights:
                dp[v][i] = min(dp[v][i], dp[u][i - 1] + w)
        return dp[dst][k + 1] if dp[dst][k + 1] != float('inf') else -1