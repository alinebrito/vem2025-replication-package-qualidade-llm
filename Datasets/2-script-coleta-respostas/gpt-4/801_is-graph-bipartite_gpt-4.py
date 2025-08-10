class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        def bfs(node):
            queue = deque([node])
            color[node] = 0
            
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        return False
            return True
        
        for i in range(len(graph)):
            if i not in color:
                if not bfs(i):
                    return False
        return True