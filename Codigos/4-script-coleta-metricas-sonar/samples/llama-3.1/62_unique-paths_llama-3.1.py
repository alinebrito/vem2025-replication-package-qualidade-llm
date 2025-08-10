class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
 def comb(a, b):
            if b > a - b:
 b = a - b
            res = 1
            for i in range(1, b + 1):
                res = res * (a - i + 1) // i
            return res
        return comb(m + n - 2, m - 1)