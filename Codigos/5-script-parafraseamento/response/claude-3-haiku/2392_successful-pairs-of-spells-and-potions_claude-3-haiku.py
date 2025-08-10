class Solution:
    def successfulPairs(self, spells, potions, success):
        n = len(spells)
        pairs = []
        for i in range(n):
            count = 0
            for j in range(n):
                if spells[i] * potions[j] >= success:
                    count += 1
            pairs.append(count)
        return pairs