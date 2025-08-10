class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            g[u].append((v, succProb[i]))
            g[v].append((u, succProb[i]))
        
        prob = [0.0] * n
        prob[start] = 1.0
        
        pq = [(1.0, start)]
        while pq:
            p, u = heapq.heappop(pq)
            if u == end:
                return p
            if p > prob[u]:
                prob[u] = p
                for v, w in g[u]:
                    heapq.heappush(pq, (p * w, v))
        
        return 0.0