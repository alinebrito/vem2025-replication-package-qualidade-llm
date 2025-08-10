class Solution:
    def repeatedStringMatch(self, a, b):
        repeat = (len(b)//len(a))
        for i in range(3):
            if b in a*(repeat+i):
                return repeat+i
        return -1