class Solution:
    def findRedundantConnection(self, edges):
        par = [i for i in range(len(edges) + 1)]
        for a, b in edges:
            pa, pb = self.find(par, a), self.find(par, b)
            if pa == pb:
                return [a, b]
            par[pa] = pb

    def find(self, par, x):
        if par[x] != x:
            par[x] = self.find(par, par[x])
        return par[x]