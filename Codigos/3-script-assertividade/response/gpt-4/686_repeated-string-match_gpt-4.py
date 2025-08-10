class Solution:
    def repeatedStringMatch(self, a, b):
        repeat = (len(b) // len(a))
        if b in a * (repeat + 2):
            return repeat + 1
        if b in a * (repeat + 1):
            return repeat + 1
        return -1