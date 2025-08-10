class Solution:
    def findCircleNum(self, isConnected):
        def dfs(city):
            for j in range(len(isConnected)):
                if isConnected[city][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1

        return provinces