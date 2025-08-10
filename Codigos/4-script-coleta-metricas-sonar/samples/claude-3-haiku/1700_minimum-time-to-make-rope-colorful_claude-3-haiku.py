class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        total_cost = 0
        for i in range(n):
            max_time = 0
            same_color_count = 0
            for j in range(i, n):
                if colors[j] == colors[i]:
                    same_color_count += 1
                    max_time = max(max_time, neededTime[j])
                else:
                    break
            total_cost += same_color_count * max_time - max_time
            i += same_color_count - 1
        return total_cost