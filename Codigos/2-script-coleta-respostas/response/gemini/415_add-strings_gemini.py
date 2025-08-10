class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1

        while p1 >= 0 or p2 >= 0 or carry > 0:
            x1 = int(num1[p1]) if p1 >= 0 else 0
            x2 = int(num2[p2]) if p2 >= 0 else 0
            current_sum = x1 + x2 + carry
            carry = current_sum // 10
            result.append(str(current_sum % 10))
            p1 -= 1
            p2 -= 1

        result.reverse()
        return ''.join(result)