class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * (len(jobs) + 1)
        
        for i in range(1, len(jobs) + 1):
            j = i - 1
            while j > 0 and jobs[j - 1][1] > jobs[i - 1][0]:
                j -= 1
            dp[i] = max(dp[i - 1], dp[j] + jobs[i - 1][2])
        
        return dp[len(jobs)]