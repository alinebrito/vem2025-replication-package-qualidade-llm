class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)
        while k:
            stack.pop()
            k -= 1
        return ''.join(stack).lstrip('0') or '0'