class Solution:
    def shortestSubarray(self, A, K):
        d = collections.deque([[0, 0]])
        n = len(A)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]
        min_length = float('inf')
        for i in range(n + 1):
            while d and prefix_sum[i] - d[0][0] >= K:
                min_length = min(min_length, i - d.popleft()[1])
            while d and d[-1][0] >= prefix_sum[i]:
                d.pop()
            d.append([prefix_sum[i], i])
        return min_length if min_length != float('inf') else -1