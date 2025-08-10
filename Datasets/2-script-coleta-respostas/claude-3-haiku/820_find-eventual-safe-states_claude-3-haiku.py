class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0] * n
        res = []

        def dfs(adj, src, vis, recst):
            if vis[src] == 1:
                return False
            if vis[src] == 2:
                return True
            vis[src] = 1
            recst.add(src)
            for nei in adj[src]:
                if nei in recst or not dfs(adj, nei, vis, recst):
                    return False
            vis[src] = 2
            recst.remove(src)
            return True

        for i in range(n):
            if dfs(graph, i, vis, set()):
                res.append(i)
        return res