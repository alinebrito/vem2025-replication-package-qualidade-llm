class Solution:
    def repeatedStringMatch(self, a, b):
        repeat = (len(b)//len(a))
        result = a * repeat
        while len(result) < len(b):
            result += a
        if b in result:
            return repeat
        if (result + a) in b:
            return repeat + 1
        return -1