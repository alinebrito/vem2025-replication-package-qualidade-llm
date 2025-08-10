class Solution:
    def __init__(self):
        pass

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        for i, (x, y) in enumerate(stones):
            for j, (dx, dy) in enumerate(stones):
                if x == dx or y == dy:
                    union(i, j)
        
        return n - len(set(find(i) for i in range(n)))