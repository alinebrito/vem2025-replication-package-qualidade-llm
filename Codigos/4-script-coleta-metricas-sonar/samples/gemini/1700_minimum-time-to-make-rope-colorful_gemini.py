class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        i = 0
        while i < len(colors) - 1:
            if colors[i] == colors[i + 1]:
                j = i + 1
                max_time = neededTime[i]
                while j < len(colors) and colors[j] == colors[i]:
                    max_time = max(max_time, neededTime[j])
                    j += 1
                total_time += sum(neededTime[i:j]) - max_time
                i = j
            else:
                i += 1
        return total_time