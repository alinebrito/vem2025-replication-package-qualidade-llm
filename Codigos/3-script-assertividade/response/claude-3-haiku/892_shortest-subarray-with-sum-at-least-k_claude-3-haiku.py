class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        d = collections.deque([[0, 0]])
        res = float('inf')
        for i in range(1, n + 1):
            while d and prefix_sum[i] - prefix_sum[d[0][0]] >= k:
                res = min(res, i - d[0][0])
                d.popleft()
            while d and prefix_sum[i] <= prefix_sum[d[-1][0]]:
                d.pop()
            d.append([i, prefix_sum[i]])
        return res if res != float('inf') else -1