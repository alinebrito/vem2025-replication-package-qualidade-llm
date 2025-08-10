class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g, dq = defaultdict(list), deque([start])
        prob = [0.0] * n
        prob[start] = 1.0
        while dq:
            u = dq.popleft()
            if u == end:
                return prob[u]
            for i, v in enumerate(g[u]):
                p = prob[u] * succProb[i]
                if p > prob[v]:
                    prob[v] = p
                    dq.append(v)
            for i, v in enumerate(edges):
                if v[0] == u:
                    g[u].append(v[1])
                elif v[1] == u:
                    g[u].append(v[0])
        return 0.0