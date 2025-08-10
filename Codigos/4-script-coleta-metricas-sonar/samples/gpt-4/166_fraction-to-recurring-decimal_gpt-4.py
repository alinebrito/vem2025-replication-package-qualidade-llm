class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        negative = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part, remainder = divmod(numerator, denominator)
        result = "-" + str(integer_part) if negative else str(integer_part)
        if remainder == 0:
            return result
        result += "."
        remainder_map = {}
        decimal_part = ""
        index = 0
        while remainder != 0:
            if remainder in remainder_map:
                decimal_part = decimal_part[:remainder_map[remainder]] + "(" + decimal_part[remainder_map[remainder]:] + ")"
                break
            remainder_map[remainder] = index
            remainder *= 10
            decimal_digit, remainder = divmod(remainder, denominator)
            decimal_part += str(decimal_digit)
            index += 1
        return result + decimal_part