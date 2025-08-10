class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        queue = deque()

        for i in range(n):
            if colors[i] != 0:
                continue
            colors[i] = 1
            queue.append(i)

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        queue.append(neighbor)