class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        result = 0
        has_center = False
        for c, freq in count.items():
            result += (freq // 2) * 2
            if freq % 2 == 1:
                has_center = True
        if has_center:
            result += 1
        return result