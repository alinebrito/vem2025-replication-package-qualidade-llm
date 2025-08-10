class Solution:
    def calcEquation(self, equations, values, queries):
        G = {}

        for (A, B), value in zip(equations, values):
            if A not in G:
                G[A] = {}
            if B not in G:
                G[B] = {}
            G[A][B] = value
            G[B][A] = 1.0 / value

        def find(x, visited):
            if x not in G:
                return -1.0
            if x not in visited:
                visited.add(x)
                for neighbor in G[x]:
                    if neighbor not in visited:
                        find(neighbor, visited)
            return G[x]

        result = []
        for C, D in queries:
            visited = set()
            C_value = find(C, visited)
            if C_value is not None and D in visited:
                result.append(C_value[D])
            else:
                result.append(-1.0)
        return result