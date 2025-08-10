class Solution:
    def numTrees(self, n: int) -> int:
        self.table = [-1] * (n+1)
        self.table[0] = 1
        return self.count(n)
    
    def count(self, n: int) -> int:
        if self.table[n] != -1:
            return self.table[n]
        sum = 0
        for i in range(1, n + 1):
            sum += self.count(i - 1) * self.count(n - i)
        self.table[n] = sum
        return sum