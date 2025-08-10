class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26  
        for task in tasks:
            count[ord(task) - ord('A')] += 1  
        max_count = max(count)
        max_tasks = count.count(max_count)
        idles = (max_count - 1) * n + (max_tasks - 1)
        total_intervals = len(tasks) + idles  
        return max(total_intervals, len(tasks))