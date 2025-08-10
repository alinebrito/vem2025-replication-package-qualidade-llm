class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        res = 0
        max_profit = 0
        i = len(jobs) - 1
        for w in sorted(worker):
            while i >= 0 and jobs[i][0] > w:
                i -= 1
            if i >= 0:
                max_profit = max(max_profit, jobs[i][1])
            res += max_profit
        return res