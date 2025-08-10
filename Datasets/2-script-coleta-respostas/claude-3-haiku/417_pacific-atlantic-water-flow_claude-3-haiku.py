class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(i, j, prev_height, visited):
            if (i, j) in visited or i < 0 or i >= m or j < 0 or j >= n or heights[i][j] < prev_height:
                return
            visited.add((i, j))
            dfs(i+1, j, heights[i][j], visited)
            dfs(i-1, j, heights[i][j], visited)
            dfs(i, j+1, heights[i][j], visited)
            dfs(i, j-1, heights[i][j], visited)
        
        for i in range(m):
            dfs(i, 0, heights[i][0], pacific)
            dfs(i, n-1, heights[i][n-1], atlantic)
        
        for j in range(n):
            dfs(0, j, heights[0][j], pacific)
            dfs(m-1, j, heights[m-1][j], atlantic)
        
        return list(pacific & atlantic)