class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        result = []
        if (numerator > 0) ^ (denominator > 0):
            result.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        n, remainder = divmod(numerator, denominator)
        result.append(str(n))
        if remainder == 0:
 return "".join(result)
        result.append(".")
        hashmap = {}
        while remainder != 0:
            if remainder in hashmap:
 start = hashmap[remainder]
                result.insert(start, "(")
                result.append(")")
                break
            hashmap[remainder] = len(result)
            n, remainder = divmod(remainder * 10, denominator)
            result.append(str(n))
 return "".join(result)