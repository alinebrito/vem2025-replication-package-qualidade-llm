class Solution:
    def isRobotBounded(self, instructions):
        direction = (0, 1)
        x = 0
        y = 0
        for i in instructions:
            if i == 'G':
                x += direction[0]
                y += direction[1]
            elif i == 'L':
                direction = (-direction[1], direction[0])
            else:
                direction = (direction[1], -direction[0])
        return (x == 0 and y == 0) or direction != (0, 1)