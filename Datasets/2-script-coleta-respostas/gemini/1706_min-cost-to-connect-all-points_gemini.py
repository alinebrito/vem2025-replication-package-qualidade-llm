class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1: List[int], p2: List[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        if n == 1:
            return 0
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = manhattan_distance(points[i], points[j])
                edges.append((dist, i, j))
        edges.sort()
        parent = list(range(n))
        rank = [1] * n
        def find(p):
            if parent[p] != p:
                parent[p] = find(parent[p])
            return parent[p]
        def union(p1, p2):
            root1, root2 = find(p1), find(p2)
            if root1 == root2:
                return False
            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]
            return True
        mst_cost = 0
        edges_used = 0
        for cost, u, v in edges:
            if union(u, v):
                mst_cost += cost
                edges_used += 1
            if edges_used == n - 1:
                break
        return mst_cost