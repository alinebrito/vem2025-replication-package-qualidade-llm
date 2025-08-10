class Solution:
    def dfs(self, adj, src, vis, recst):
        vis[src] = 1
        recst[src] = 1
        for i in adj[src]:
            if not vis[i]:
                self.dfs(adj, i, vis, recst)
            elif recst[i]:
                recst[src] = 0

    def eventualSafeNodes(self, graph):
        n = len(graph)
        vis = [0] * n
        recst = [0] * n
        for i in range(n):
            if not vis[i]:
                self.dfs(graph, i, vis, recst)
        return [i for i in range(n) if recst[i]]