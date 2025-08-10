class Solution:
    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'G':
                x, y = x + dx, y + dy
            elif i == 'L':
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)