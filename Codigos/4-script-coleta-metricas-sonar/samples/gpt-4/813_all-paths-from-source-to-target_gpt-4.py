class Solution:
    def allPathsSourceTarget(self, graph):
        def backtrack(node, path):
            if node == len(graph) - 1:
                paths.append(path)
                return
            for neighbor in graph[node]:
                backtrack(neighbor, path + [neighbor])
        
        paths = []
        backtrack(0, [0])
        return paths