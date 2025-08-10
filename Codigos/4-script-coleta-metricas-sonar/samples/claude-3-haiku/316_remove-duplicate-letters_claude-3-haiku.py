class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_index = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in stack:
                while stack and c < stack[-1] and last_index[stack[-1]] > i:
                    stack.pop()
                stack.append(c)
        return ''.join(stack)