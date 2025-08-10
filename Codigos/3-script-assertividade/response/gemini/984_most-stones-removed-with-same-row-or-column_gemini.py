class Solution:
    def removeStones(self, stones):
        n = len(stones)
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if rank[px] > rank[py]:
                    parent[py] = px
                    rank[px] += rank[py]
                else:
                    parent[px] = py
                    rank[py] += rank[px]

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)

        num_groups = sum(1 for i in range(n) if parent[i] == i)
        return n - num_groups