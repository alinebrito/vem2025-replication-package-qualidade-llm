class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edgeMap = [[] for _ in range(n)]
        for u, v in connections:
            edgeMap[u].append(v)
            edgeMap[v].append(u)
        
        low = [0] * n
        disc = [0] * n
        visited = [False] * n time = 0
        critical = []
 def dfs(node, parent):
            nonlocal time
            visited[node] = True
            low[node] = disc[node] = time
            time += 1
            for neighbor in edgeMap[node]:
                if not visited[neighbor]:
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        critical.append([node, neighbor])
                elif neighbor != parent:
                    low[node] = min(low[node], disc[neighbor])
        
        for i in range(n):
            if not visited[i]:
                dfs(i, -1)
        
        return critical