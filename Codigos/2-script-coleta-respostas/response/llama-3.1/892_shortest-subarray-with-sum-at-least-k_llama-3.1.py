class Solution:
    def shortestSubarray(self, A, K):
        d = collections.deque([[0, 0]])
        s = 0
        ans = float('inf')
        for i, x in enumerate(A):
            s += x
            while d and s - d[0][0] >= K:
                ans = min(ans, i - d[0][1])
                s -= d.popleft()[0]
            while d and d[-1][0] >= s:
                d.pop()
            d.append([s, i])
        return ans if ans != float('inf') else -1