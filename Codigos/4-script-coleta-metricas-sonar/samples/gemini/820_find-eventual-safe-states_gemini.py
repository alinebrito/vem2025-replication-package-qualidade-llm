class Solution:
    def dfs(self, adj, src, vis, recst):
        vis[src] = 1
        recst[src] = 1
        for v in adj[src]:
            if not vis[v]:
                if self.dfs(adj, v, vis, recst):
                    return True
            elif recst[v]:
                return True
        recst[src] = 0
        return False

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        vis = [0] * n
        recst = [0] * n
        for i in range(n):
            if not vis[i]:
                self.dfs(graph, i, vis, recst)
        safe = []
        for i in range(n):
            if not recst[i]:
                safe.append(i)
        return safe