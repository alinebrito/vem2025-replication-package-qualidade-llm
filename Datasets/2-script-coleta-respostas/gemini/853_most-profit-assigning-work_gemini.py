class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        n, m = len(jobs), len(worker)
        i = j = total_profit = best_profit = 0
        while j < m:
            while i < n and jobs[i][0] <= worker[j]:
                best_profit = max(best_profit, jobs[i][1])
                i += 1
            total_profit += best_profit
            j += 1
        return total_profit