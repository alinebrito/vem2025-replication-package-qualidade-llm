class Solution:
    def trailingZeroes(self, n: int) -> int:
        r = 0
        i = 5
        while n // i >= 1:
            r += n // i
            i *= 5
        return r