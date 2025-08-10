class Solution:
    def min_cost_connect_points(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        parent = list(range(n))
        rank = [0] * n
        cost = [float('inf')] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y, w):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx
                else:
                    parent[rootx] = rooty
                    if rank[rootx] == rank[rooty]:
                        rank[rooty] += 1
                cost[rootx] = min(cost[rootx], w)

        for i in range(n):
            cost[i] = 0
        for i in range(n):
            for j in range(i + 1, n):
                w = manhattan_distance(points[i], points[j])
                union(i, j, w)
        return max(cost)