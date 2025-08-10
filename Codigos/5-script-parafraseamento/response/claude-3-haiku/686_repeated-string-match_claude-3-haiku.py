class Solution:
    def repeatedStringMatch(self, a, b):
        repeat = (len(b) // len(a)) + 1
        result = a * repeat
        if b in result:
            return repeat
        else: