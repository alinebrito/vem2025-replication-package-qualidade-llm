class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1
        
        extra_edges = len(connections) - (n - 1)
        if extra_edges < components - 1:
            return -1