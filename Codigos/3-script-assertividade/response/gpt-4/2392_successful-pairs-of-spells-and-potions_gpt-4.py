class Solution:
    def successfulPairs(self, spells, potions, success):
        n = len(spells)
        pairs = []
        for i in range(n):
            count = 0
            for potion in potions:
                if spells[i] * potion >= success:
                    count += 1
            pairs.append(count)
        return pairs