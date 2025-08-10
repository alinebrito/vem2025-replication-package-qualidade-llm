class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        from collections import defaultdict
        from heapq import heappop, heappush
        
        g = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            g[a].append((b, prob))
            g[b].append((a, prob))
        
        max_prob = [0] * n
        max_prob[start] = 1
        pq = [(-1, start)]
        
        while pq:
            prob, node = heappop(pq)
            prob = -prob
            
            if node == end:
                return prob
            
            for neighbor, edge_prob in g[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heappush(pq, (-new_prob, neighbor))
        
        return 0