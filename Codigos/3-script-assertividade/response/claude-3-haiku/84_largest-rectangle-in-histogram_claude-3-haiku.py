class Solution:
    def largestRectangleArea(self, heights):
        height = heights[:]
        height.append(0)
        stack = [-1]
        max_area = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area