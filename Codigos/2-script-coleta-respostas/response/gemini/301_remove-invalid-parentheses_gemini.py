class Solution:
    def removeInvalidParentheses(self, s):
        level = {s}
        while True:
            valid = []
            for s in level:
                if self.isValid(s):
                    valid.append(s)
            if valid:
                return valid
            next_level = set()
            for s in level:
                for i in range(len(s)):
                    next_level.add(s[:i] + s[i+1:])
            level = next_level

    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0