class Solution:
    def shortestSubarray(self, A, K):
        d = [[0, 0]]
        res = float('inf')
        s = 0
        for i, a in enumerate(A):
            s += a
            while d and s - d[0][0] >= K:
                res = min(res, i + 1 - d.pop(0)[1])
            idx = len(d)
            while idx and s <= d[idx - 1][0]:
                idx -= 1
            d.insert(idx, [s, i + 1])
        return res if res < float('inf') else -1