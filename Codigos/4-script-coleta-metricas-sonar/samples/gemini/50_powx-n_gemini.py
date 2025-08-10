class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1.0 / x
            n = -n
        result = 1.0
        while n:
            if n & 1:  # Check if last bit is 1 using bitwise AND
                result *= x
            x *= x
            n >>= 1  # Right shift n by 1 bit
        return result