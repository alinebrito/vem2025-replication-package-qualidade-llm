class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        vowels = set('aeiou')
        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        ans = curr
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr += 1
            if s[i - k] in vowels:
                curr -= 1
            ans = max(ans, curr)
        return ans