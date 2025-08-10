class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        max_profit = 0
        max_profit_so_far = 0
        j = 0
        
        for ability in sorted(worker):
            while j < len(jobs) and jobs[j][0] <= ability:
                max_profit_so_far = max(max_profit_so_far, jobs[j][1])
                j += 1
            max_profit += max_profit_so_far
        
        return max_profit