class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque([source])
        visited = [False] * n
        visited[source] = True
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        
        return False