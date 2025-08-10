class Solution:
    def leastInterval(self, tasks, n):
        task_count = [0] * 26  
        for task in tasks:
            task_count[ord(task) - ord('A')] += 1  
        max_count = max(task_count)
        max_count_tasks = task_count.count(max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)