class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        dp = [0] * (len(jobs) + 1)
        for i in range(len(jobs)):
            j = i - 1
            while j >= 0 and jobs[i][1] < jobs[j][0]:
                j -= 1
            dp[i + 1] = max(dp[i], dp[j + 1] + jobs[i][2])
        return dp[-1]