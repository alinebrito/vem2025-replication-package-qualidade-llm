class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * n
        queue = [source]
        visited[source] = True

        while queue:
            curr = queue.pop(0)
            if curr == destination:
                return True
            for neighbor in adj_list[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False