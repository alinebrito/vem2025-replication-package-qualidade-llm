class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        count = Counter(deck)
        g = -1
        for x in count.values():
            if g == -1:
                g = x
            else:
                g = self.gcd(g, x)
        return g >= 2

    def gcd(self, x, y):
        while y:
            x, y = y, x % y