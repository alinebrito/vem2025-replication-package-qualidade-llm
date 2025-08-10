class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        count.sort(reverse=True)
        max_val = count[0] - 1
        idle_slots = max_val * n
        for i in range(1, 26):
            idle_slots -= min(max_val, count[i])
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)