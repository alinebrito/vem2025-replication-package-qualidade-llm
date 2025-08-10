class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        counts = list(Counter(deck).values())
        for x in range(2, min(counts) + 1):
            if all(count % x == 0 for count in counts):
                return True
        return min(counts) > 1