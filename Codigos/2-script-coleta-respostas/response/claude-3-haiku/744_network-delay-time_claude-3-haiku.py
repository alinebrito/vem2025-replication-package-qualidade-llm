class Solution:
    def networkDelayTime(self, times, N, K):
        q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for nei, dur in adj[node]:
                    heapq.heappush(q, (time + dur, nei))
        return max(t.values()) if len(t) == N else -1