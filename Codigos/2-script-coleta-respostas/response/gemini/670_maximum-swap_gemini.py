class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        for i in range(n - 1):
            max_idx = i
            for j in range(i + 1, n):
                if int(s[j]) >= int(s[max_idx]):
                    max_idx = j
            if int(s[max_idx]) > int(s[i]):
                s[i], s[max_idx] = s[max_idx], s[i]
                return int("".join(s))
        return num