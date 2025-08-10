class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        self.u = list(range(n))
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    self.union(i, j)
        return len(set(self.find(i) for i in range(n)))

    def find(self, x):
        if self.u[x] != x:
            self.u[x] = self.find(self.u[x])
        return self.u[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.u[rx] = ry