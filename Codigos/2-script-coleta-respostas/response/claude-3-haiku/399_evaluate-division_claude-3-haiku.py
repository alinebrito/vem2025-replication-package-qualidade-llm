class Solution:
    def calcEquation(self, equations, values, queries):
        G = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            G[a][b] = v
            G[b][a] = 1 / v

        def dfs(node, target, visited):
            if node not in G or target not in G:
                return -1.0
            if target in G[node]:
                return G[node][target]
            visited.add(node)
            for nei in G[node]:
                if nei not in visited:
                    res = dfs(nei, target, visited)
                    if res != -1.0:
                        return G[node][nei] * res
            return -1.0

        return [dfs(a, b, set()) for a, b in queries]