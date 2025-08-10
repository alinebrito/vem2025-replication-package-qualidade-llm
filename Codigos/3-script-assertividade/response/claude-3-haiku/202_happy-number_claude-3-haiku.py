class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n != 1:
            if n in mem:
                return False
            mem.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return True