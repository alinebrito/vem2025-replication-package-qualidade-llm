class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(endTime, startTime, profit))
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            end, start, p = jobs[i - 1]
            j = bisect.bisect_right(jobs, (start, 0, float('-inf')))
            dp[i] = max(dp[i - 1], dp[j] + p)
        return dp[n]