class Solution(object):
    def customSortString(self, order, s):
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        result = []
        for c in order:
            if c in count:
                result.extend([c] * count[c])
                del count[c]
        for c in count:
            result.extend([c] * count[c])
        return "".join(result)