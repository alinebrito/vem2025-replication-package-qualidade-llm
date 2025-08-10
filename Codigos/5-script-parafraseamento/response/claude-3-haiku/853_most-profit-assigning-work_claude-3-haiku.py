class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        res = 0
        max_profit = 0
        i = 0
        for w in sorted(worker):
            while i < len(jobs) and w >= jobs[i][0]:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            res += max_profit