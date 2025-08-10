class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit), key=lambda x: x[0])
        worker.sort()
        max_profit = 0
        max_profit_so_far = 0
        j = 0
        for w in worker:
            while j < len(jobs) and jobs[j][0] <= w:
                max_profit_so_far = max(max_profit_so_far, jobs[j][1])
                j += 1
            max_profit += max_profit_so_far
        return max_profit