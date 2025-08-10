class Solution:
    def numTrees(self, n: int) -> int:
        self.table = [-1] * (n+1)
        return self.helper(n)

    def helper(self, n: int) -> int:
        if self.table[n] != -1:
            return self.table[n]
        if n == 0 or n == 1:
            return 1
        res = 0
        for i in range(1, n+1):
            left = self.helper(i-1)
            right = self.helper(n-i)
            res += left * right
        self.table[n] = res
        return res