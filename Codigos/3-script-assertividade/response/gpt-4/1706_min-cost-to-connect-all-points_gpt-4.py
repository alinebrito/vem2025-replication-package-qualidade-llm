class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1: List[int], p2: List[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        n = len(points)
        visited = [False] * n
        min_heap = [(0, 0)]
        total_cost = 0
        edges_used = 0
        
        while edges_used < n:
            cost, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += cost
            edges_used += 1
            
            for v in range(n):
                if not visited[v]:
                    heapq.heappush(min_heap, (manhattan_distance(points[u], points[v]), v))
        
        return total_cost