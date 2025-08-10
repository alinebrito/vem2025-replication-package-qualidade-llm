class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(capital, profits), reverse=True)
        available = []
        while k > 0:
            while projects and projects[-1][0] <= w:
                c, p = projects.pop()
                heappush(available, -p)
            if available:
                w -= heappop(available)
                k -= 1
            else:
                break
        return w