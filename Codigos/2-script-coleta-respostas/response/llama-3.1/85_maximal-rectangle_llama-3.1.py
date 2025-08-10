class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        height = [0] * n
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            stack = []
            for k in range(n + 1):
                if k < n:
                    if height[k] == 0:
                        stack = []
                    else:
                        while stack and height[stack[-1]] >= height[k]:
                            h = height[stack.pop()]
                            w = k if not stack else k - stack[-1] - 1
                            max_area = max(max_area, h * w)
                        stack.append(k)
                else:
                    while stack:
                        h = height[stack.pop()]
                        w = n if not stack else n - stack[-1] - 1
                        max_area = max(max_area, h * w)
        return max_area