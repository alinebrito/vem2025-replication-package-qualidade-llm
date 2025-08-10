class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = {}
        for task in tasks:
            if task in task_counts:
                task_counts[task] += 1
            else:
                task_counts[task] = 1
        
        max_count = max(task_counts.values())
        max_count_tasks = sum(count == max_count for count in task_counts.values())
        
        ans = (max_count - 1) * (n + 1)
        ans += max_count_tasks
        
        return max(len(tasks), ans)