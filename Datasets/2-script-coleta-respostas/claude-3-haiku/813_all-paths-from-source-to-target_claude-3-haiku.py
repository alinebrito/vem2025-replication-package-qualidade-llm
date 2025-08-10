class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        paths = []

        def dfs(node, path):
            if node == n - 1:
                paths.append(path[:])
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

        dfs(0, [0])
        return paths