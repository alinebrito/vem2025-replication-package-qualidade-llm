class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
 seen = [True] * n
        seen[0] = seen[1] = False
        p = 2
        while p * p < n:
 if seen[p]:
                for i in range(p * p, n, p):
                    seen[i] = False
            p += 1
        return sum(seen)