class Solution:
    def numTrees(self, n: int) -> int:
        self.table = [-1] * (n+1)

        def dp(n):
            if n == 0 or n == 1:
                return 1
            if self.table[n] != -1:
                return self.table[n]
            res = 0
            for i in range(1, n + 1):
                res += dp(i - 1) * dp(n - i)
            self.table[n] = res
            return res

        return dp(n)