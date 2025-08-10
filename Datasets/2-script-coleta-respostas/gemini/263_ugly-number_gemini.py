class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False
        for p in [2, 3, 5]:
            while num % p == 0:
                num //= p