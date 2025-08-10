class Solution:
    def trailingZeroes(self, n):
        r = 0
        while n > 0:
            n //= 5
            r += n
        return r