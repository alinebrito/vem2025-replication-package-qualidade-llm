class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        result = []
        for char in S:
            if char == '(':
                if count > 0:
                    result.append(char)
                count += 1
            else:
                count -= 1
                if count > 0:
                    result.append(char)
        return ''.join(result)