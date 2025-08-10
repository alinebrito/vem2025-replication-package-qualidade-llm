class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(g))) + k for k, g in groupby(s))
        return s