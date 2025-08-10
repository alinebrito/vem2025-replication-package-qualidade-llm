class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        edges.sort()
        
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        cost = 0
        for w, i, j in edges:
            if find(i) != find(j):
                union(i, j)
                cost += w
        
        return cost