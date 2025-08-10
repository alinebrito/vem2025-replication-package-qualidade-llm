class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        vis = [0] * n
        safe = [0] * n
        
        def dfs(src):
            if vis[src] != 0:
                return vis[src] == 2
            vis[src] = 1
            for neighbor in graph[src]:
                if not dfs(neighbor):
                    return False
            vis[src] = 2
            return True
        
        for i in range(n):
            dfs(i)
        
        return sorted(i for i in range(n) if vis[i] == 2)