class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = (len(b) - 1) // len(a) + 1
        for i in range(2):
            if b in a * (repeat + i):
                return repeat + i
        return -1