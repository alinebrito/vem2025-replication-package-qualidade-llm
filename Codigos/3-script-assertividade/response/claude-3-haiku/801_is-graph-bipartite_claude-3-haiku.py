class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        
        def dfs(node, color=0):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    if not dfs(neighbor, color ^ 1):
                        return False
                elif colors[neighbor] == color:
                    return False
            return True
        
        for node in range(n):
            if colors[node] == -1:
                if not dfs(node):
                    return False
        
        return True