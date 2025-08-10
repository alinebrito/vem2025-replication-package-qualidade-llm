class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        last = {x: i for i, x in enumerate(s)}
        for i, x in enumerate(s):
            if x == max(s[i:]):
                continue
            for d in range(9, int(x) - 1, -1):
                d = str(d)
                if d in last and last[d] > i:
                    s[i], s[last[d]] = s[last[d]], s[i]
                    return int(''.join(s))
        return num