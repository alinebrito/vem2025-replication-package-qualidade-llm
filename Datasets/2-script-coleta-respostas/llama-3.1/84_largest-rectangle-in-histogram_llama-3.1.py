class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = []
        max_area = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area