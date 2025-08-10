class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        a, b = s[:len(s)//2], s[len(s)//2:]
        return sum(1 for char in a if char in vowels) == sum(1 for char in b if char in vowels)