class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        stack = []
        for digit in num:
            while stack and int(stack[-1]) > int(digit) and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        result = "".join(stack)
        result = result.lstrip('0')
        return result if result else "0"