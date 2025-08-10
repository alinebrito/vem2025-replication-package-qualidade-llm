class Solution:
    def countPrimes(self, n: int) -> int:
        seen, ans = [0] * n, 0
        for i in range(2, n):
            if seen[i]:
                continue
            ans += 1
            for j in range(i * i, n, i):
                seen[j] = 1
        return ans