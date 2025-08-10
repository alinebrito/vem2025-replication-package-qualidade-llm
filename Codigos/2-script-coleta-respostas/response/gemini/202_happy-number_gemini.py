class Solution:
    def isHappy(self, n):
        mem = set()
        while n not in mem:
            mem.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1