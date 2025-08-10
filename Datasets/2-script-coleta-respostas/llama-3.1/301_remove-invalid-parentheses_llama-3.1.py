class Solution:
    def removeInvalidParentheses(self, s):
        level = {s}
        while True:
            valid = set(filter(self.isValid, level))
            if valid:
                return list(valid)
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in '()':
                        next_level.add(item[:i] + item[i+1:])
            level = next_level

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