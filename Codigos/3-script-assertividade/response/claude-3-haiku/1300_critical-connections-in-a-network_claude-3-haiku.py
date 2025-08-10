class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edgeMap = defaultdict(list)
        for u, v in connections:
            edgeMap[u].append(v)
            edgeMap[v].append(u)
        
        visited = [False] * n
        low = [float('inf')] * n
        disc = [float('inf')] * n
        parent = [-1] * n
        time = 0
        result = []
        
        def dfs(u):
            nonlocal time
            visited[u] = True
            disc[u] = low[u] = time
            time += 1
            
            for v in edgeMap[u]:
                if not visited[v]:
                    parent[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        result.append([u, v])
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        return result