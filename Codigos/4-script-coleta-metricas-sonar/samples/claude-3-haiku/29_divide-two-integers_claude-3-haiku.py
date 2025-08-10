class Solution:
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while (temp << 1) <= dividend:
                temp <<= 1
                i <<= 1
            dividend -= temp
            res += i
        return res if positive else -res