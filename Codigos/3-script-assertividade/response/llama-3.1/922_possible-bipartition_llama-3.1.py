class Solution:
    def possibleBipartition(self, N: int, dislikes: list[list[int]]) -> bool:
        graph = [[] for _ in range(N + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [0] * (N + 1)

        def dfs(node: int, c: int) -> bool:
            if color[node]:
                return color[node] == c
            color[node] = c
            for neighbor in graph[node]:
                if not dfs(neighbor, -c):
                    return False
            return True

        for i in range(1, N + 1):
            if not color[i]:
                if not dfs(i, 1):
                    return False
        return True