class Solution(object):
    def removeStars(self, s):
        stack = []
        for c in s:
            if c != '*':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
        return ''.join(stack)