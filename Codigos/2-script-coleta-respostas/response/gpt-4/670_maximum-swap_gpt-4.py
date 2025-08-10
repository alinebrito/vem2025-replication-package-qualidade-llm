class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        last = {int(x): i for i, x in enumerate(s)}
        for i in range(len(s)):
            for d in range(9, int(s[i]), -1):
                if d in last and last[d] > i:
                    s[i], s[last[d]] = s[last[d]], s[i]
                    return int(''.join(s))
        return num  