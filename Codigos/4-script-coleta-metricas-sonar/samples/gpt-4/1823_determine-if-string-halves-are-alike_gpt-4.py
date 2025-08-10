class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        vowels = set('aeiouAEIOU')
        return sum(1 for char in a if char in vowels) == sum(1 for char in b if char in vowels)