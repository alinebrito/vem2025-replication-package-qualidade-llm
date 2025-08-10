class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        to_remove = set()
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        to_remove.update(stack)
        return ''.join(char for i, char in enumerate(s) if i not in to_remove)