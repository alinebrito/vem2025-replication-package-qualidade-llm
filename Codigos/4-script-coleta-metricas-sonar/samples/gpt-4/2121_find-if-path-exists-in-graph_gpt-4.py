class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        stack = [source]
        
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(graph[node])
        
        return False