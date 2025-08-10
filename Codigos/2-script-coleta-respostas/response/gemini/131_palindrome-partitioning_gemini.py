class Solution:
    def partition(self, s):
        if not s: return [[]]
        res = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for rest in self.partition(s[i:]):
                    res.append([s[:i]] + rest)
        return res