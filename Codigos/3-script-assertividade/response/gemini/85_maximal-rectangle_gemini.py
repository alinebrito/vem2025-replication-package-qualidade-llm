class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        max_area = 0
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            stack = [-1]
            for j in range(n + 1):
                while heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(j)
        return max_area