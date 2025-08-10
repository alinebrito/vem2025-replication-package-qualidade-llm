class Solution:
    def calcEquation(self, equations, values, queries):
        G = collections.defaultdict(dict)
        for (A, B), value in zip(equations, values):
            G[A][B] = value
            G[B][A] = 1 / value
        def dfs(start, end, visited):
            if start == end:
                return 1.0
            if start not in G or end not in G:
                return -1.0
            for neighbor, value in G[start].items():
                if neighbor not in visited:
                    visited.add(neighbor)
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result
            return -1.0
        results = []
        for C, D in queries:
            results.append(dfs(C, D, set()))
        return results