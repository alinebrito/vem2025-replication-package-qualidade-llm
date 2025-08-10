class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    dfs(j)

        n = len(isConnected)
        visited = [False] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1
        return res