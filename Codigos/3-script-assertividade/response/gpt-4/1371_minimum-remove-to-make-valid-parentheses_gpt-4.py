class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        open_count = 0
        for char in s:
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count == 0:
                    s.remove(char)
                else:
                    open_count -= 1
        for i in range(len(s) - 1, -1, -1):
            if open_count == 0:
                break
            if s[i] == '(':
                s.remove('(')
                open_count -= 1
        return ''.join(s)