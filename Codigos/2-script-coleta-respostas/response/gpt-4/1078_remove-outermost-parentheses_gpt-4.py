class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []
        
        for char in s:
            if char == '(':
                stack.append(char)
                if len(stack) > 1:
                    result.append(char)
            else:
                stack.pop()
                if len(stack) > 0:
                    result.append(char)
        
        return "".join(result)