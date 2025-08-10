class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        a_count = 0
        b_count = 0
        n = len(s) // 2
        for i in range(n):
            if s[i] in vowels:
                a_count += 1
        for i in range(n, len(s)):
            if s[i] in vowels:
                b_count += 1
        return a_count == b_count