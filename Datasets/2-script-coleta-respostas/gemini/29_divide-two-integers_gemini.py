class Solution:
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp = divisor
            shift = 1
            while dividend >= temp << shift:
                temp <<= shift
                shift += 1
            quotient += 1 << (shift - 1)
            dividend -= temp

        if not positive:
            quotient = -quotient
        return min(max(quotient, -2**31), 2**31 - 1)