class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10
        if reversed_num > 2**31 - 1:
            return 0
        return sign * reversed_num