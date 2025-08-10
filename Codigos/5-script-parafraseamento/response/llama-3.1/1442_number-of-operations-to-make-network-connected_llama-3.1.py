class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        p = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if x!= p[x]: p[x] = find(p[x])
            return p[x]

        def union(x, y):
            x_root, y_root = find(x), find(y)
            if x_root == y_root: return 0
            if rank[x_root] < rank[y_root]: x_root, y_root = y_root, x_root
            rank[x_root] += rank[y_root]
            p[y_root] = x_root
            return 1

        count = n
        for x, y in connections: count -= union(x, y)
        return count - 1