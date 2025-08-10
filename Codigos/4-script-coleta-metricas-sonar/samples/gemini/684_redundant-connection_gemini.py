class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                par[rx] = ry
                return True
            return False
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]