class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        
        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            
            stack = []
            for j in range(cols + 1):
                while stack and heights[stack[-1]] > heights[j]:
                    h = heights[stack.pop()]
                    w = j if not stack else j - stack[-1] - 1  
                    max_area = max(max_area, h * w)
                stack.append(j)
        
        return max_area  