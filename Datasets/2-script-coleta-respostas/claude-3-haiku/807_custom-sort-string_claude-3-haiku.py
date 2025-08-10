class Solution(object):
    def customSortString(self, order, s):
        res = []
        for c in order:
            res.append(c * s.count(c))
        for c in s:
            if c not in order:
                res.append(c)
        return ''.join(res)