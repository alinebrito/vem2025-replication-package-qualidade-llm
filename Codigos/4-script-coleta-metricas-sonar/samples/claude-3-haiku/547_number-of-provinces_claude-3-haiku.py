class Solution:
    def __init__(self, n):
        self.u = list(range(n))

    def find(self, x):
        if self.u[x] != x:
            self.u[x] = self.find(self.u[x])
        return self.u[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        self.u[xroot] = yroot

    def numProvinces(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    self.union(i, j)
        return sum(self.u[i] == i for i in range(n))