class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        total_time = 0
        max_time = 0
        for i in range(n):
            max_time = max(max_time, neededTime[i])
            total_time += max_time
        return total_time - max(neededTime)