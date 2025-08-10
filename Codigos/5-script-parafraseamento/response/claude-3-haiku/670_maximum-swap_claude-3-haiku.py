class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        max_idx = len(s) - 1
        max_digit = s[-1]
        for i in range(len(s) - 2, -1, -1):
            if s[i] > max_digit:
                max_digit = s[i]
                max_idx = i
            elif s[i] < max_digit:
                s[i], s[max_idx] = s[max_idx], s[i]
                return int(''.join(s))