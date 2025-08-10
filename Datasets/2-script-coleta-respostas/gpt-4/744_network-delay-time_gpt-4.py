class Solution:
    def networkDelayTime(self, times, N, K):
        q, t, adj = [(0, K)], {}, {}
        for u, v, w in times:
            adj[u] = adj.get(u, []) + [(v, w)]
        while q:
            time, node = q.pop(0)
            if node not in t:
                t[node] = time
                for v, w in adj.get(node, []):
                    q.append((time + w, v))
        return max(t.values()) if len(t) == N else -1