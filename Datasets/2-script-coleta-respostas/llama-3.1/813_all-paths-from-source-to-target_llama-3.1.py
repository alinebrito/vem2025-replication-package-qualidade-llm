class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        res = []
        def dfs(node, path):
            if node == n - 1:
                res.append(path)
                return
            for next_node in graph[node]:
                dfs(next_node, path + [next_node])
        dfs(0, [0])
        return res