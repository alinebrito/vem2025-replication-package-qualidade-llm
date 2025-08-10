class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [0] * len(jobs)
        dp[0] = jobs[0][2]
        for i in range(1, len(jobs)):
            dp[i] = max(dp[i-1], jobs[i][2])
            for j in range(i-1, -1, -1):
                if jobs[j][1] <= jobs[i][0]:
                    dp[i] = max(dp[i], dp[j] + jobs[i][2])
                    break
        return dp[-1]