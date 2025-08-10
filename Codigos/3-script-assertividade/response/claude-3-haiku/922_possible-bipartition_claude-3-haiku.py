class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(N+1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = [0] * (N+1)
        
        def dfs(node, c=1):
            if color[node]:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, -c) for nei in graph[node])
        
        return all(dfs(node) for node in range(1, N+1) if not color[node])