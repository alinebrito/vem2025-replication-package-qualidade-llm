class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            par[px] = py
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]