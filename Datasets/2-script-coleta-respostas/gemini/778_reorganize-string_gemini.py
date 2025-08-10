class Solution:
    def reorganizeString(self, S):
        if not S:
            return ""
        count = {}
        for c in S:
            count[c] = count.get(c, 0) + 1
        max_freq = max(count.values())
        if max_freq > (len(S) + 1) // 2:
            return ""
        result = [""] * len(S)
        even, odd = 0, 1
        for c in sorted(count, key=count.get, reverse=True):
            while count[c] > 0 and even < len(S):
                result[even] = c
                count[c] -= 1
                even += 2
            while count[c] > 0 and odd < len(S):
                result[odd] = c
                count[c] -= 1
                odd += 2
        return "".join(result)