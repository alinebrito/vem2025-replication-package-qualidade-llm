class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        if n == 1:
            return 0

        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        min_heap = []
        for i in range(n):
            heapq.heappush(min_heap, (0, i))

        total_cost = 0
        visited = [False] * n

        while min_heap:
            cost, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += cost

            for v in range(n):
                if not visited[v]:
                    heapq.heappush(min_heap, (manhattan_distance(points[u], points[v]), v))

        return total_cost