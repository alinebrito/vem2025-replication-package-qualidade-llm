class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        from collections import defaultdict, deque
        g, dq = defaultdict(list), deque([start])
        for a, b, p in zip(edges, edges[1:], succProb):
            g[a].append((b, p))
            g[b].append((a, p))

        prob = [0] * n
        prob[start] = 1

        while dq:
            u = dq.popleft()
            for v, p in g[u]:
                if prob[v] < p * prob[u]:
                    prob[v] = p * prob[u]
                    dq.append(v)

        return prob[end]