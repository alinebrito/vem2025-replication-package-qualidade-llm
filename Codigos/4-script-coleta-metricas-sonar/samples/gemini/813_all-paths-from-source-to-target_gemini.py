class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        result = []

        def dfs(node, path):
            if node == n - 1:
                result.append(path.copy())
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

        dfs(0, [0])
        return result