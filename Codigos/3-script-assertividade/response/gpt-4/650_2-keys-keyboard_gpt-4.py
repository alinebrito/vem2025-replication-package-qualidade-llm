class Solution:
    def minSteps(self, n: int) -> int:
        steps, d = 0, 2
        while d <= n:
            while n % d == 0:
                steps += d
                n /= d
            d += 1
        return steps