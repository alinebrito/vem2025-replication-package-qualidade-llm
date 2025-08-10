class Solution:
    def calcEquation(self, equations, values, queries):
        G = {}
        for (u, v), value in zip(equations, values):
            if u not in G:
                G[u] = {}
            if v not in G:
                G[v] = {}
            G[u][v] = value  
            G[v][u] = 1 / value
            
        def bfs(start, end):
            if start not in G or end not in G:
                return -1.0  
            queue = [(start, 1.0)]
            visited = {start}
            while queue:
                node, product = queue.pop(0)
                if node == end:
                    return product  
                for neighbor in G[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product * G[node][neighbor]))
            return -1.0
        
        return [bfs(c, d) for c, d in queries]