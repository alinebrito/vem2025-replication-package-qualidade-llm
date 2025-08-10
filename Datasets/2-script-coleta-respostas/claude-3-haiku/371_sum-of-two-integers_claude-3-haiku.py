class Solution:
    def getSum(self, a: int, b: int) -> int:
        if b == 0:
            return a
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a