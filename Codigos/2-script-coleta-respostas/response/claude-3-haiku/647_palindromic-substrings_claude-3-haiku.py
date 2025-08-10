class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            count += 1
            left, right = i - 1, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count