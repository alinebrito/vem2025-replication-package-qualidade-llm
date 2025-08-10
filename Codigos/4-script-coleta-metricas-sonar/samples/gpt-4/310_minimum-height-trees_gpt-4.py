class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0]
        from collections import defaultdict, deque  
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves  
        return leaves  