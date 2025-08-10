class Solution:
    def fractionToDecimal(self, numerator, denominator):
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = sign + str(n)
        if remainder == 0:
            return result
        result += '.'
        seen = {}
        while remainder != 0:
            if remainder in seen:
                idx = seen[remainder]
                return result[:idx] + '(' + result[idx:] + ')'
            seen[remainder] = len(result)
            remainder *= 10
            digit, remainder = divmod(remainder, abs(denominator))
            result += str(digit)
        return result