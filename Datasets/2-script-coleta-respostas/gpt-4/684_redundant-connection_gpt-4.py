class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        for edge in edges:
            u, v = edge  
            pu, pv = find(u), find(v)
            if pu == pv:
                res = edge  
            else:
                par[pu] = pv
        
        return res  