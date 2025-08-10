class Solution:
    def numTrees(self, n: int) -> int:
        self.table = [-1] * (n + 1)
        self.table[0], self.table[1] = 1, 1
        
        for i in range(2, n + 1):
            total = 0  
            for j in range(1, i + 1):
                total += self.table[j - 1] * self.table[i - j]
            self.table[i] = total
            
        return self.table[n]