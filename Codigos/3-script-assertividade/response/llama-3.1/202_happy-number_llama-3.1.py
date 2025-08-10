class Solution:
    def isHappy(self, n):
        mem = set()
        while n != 1 and n not in mem:
            mem.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1