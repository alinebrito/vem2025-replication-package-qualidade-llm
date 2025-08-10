class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                res += i
                n //= i
        if n > 1:
            res += n
        return res