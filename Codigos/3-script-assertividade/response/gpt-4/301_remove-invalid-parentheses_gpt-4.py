class Solution:
    def removeInvalidParentheses(self, s):
        level = {s}
        while True:
            valid = set(filter(self.isValid, level))
            if valid:
                return list(valid)
            level = {self.removeOne(p) for p in level}

    def isValid(self, s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    def removeOne(self, s):
        return {s[:i] + s[i + 1:] for i in range(len(s)) if s[i] in '()'}