class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '0':
                    heights[col] = 0
                else:
                    heights[col] += 1
            
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        for i, height in enumerate(heights + [0]):
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        
        return max_area