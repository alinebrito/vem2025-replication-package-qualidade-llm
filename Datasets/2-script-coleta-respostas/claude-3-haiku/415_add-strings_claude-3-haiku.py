class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            total = digit1 + digit2 + carry
            carry = total // 10
            result = str(total % 10) + result
            i -= 1
            j -= 1
        return result