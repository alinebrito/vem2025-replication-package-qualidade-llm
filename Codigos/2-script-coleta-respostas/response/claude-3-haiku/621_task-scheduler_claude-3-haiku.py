class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = collections.Counter(tasks)
        max_count = max(task_count.values())
        num_max_count = sum(1 for count in task_count.values() if count == max_count)
        return max((max_count - 1) * (n + 1) + num_max_count, len(tasks))