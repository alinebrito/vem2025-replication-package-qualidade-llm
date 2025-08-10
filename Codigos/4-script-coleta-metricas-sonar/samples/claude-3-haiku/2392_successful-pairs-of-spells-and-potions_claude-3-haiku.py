class Solution:
    def successfulPairs(self, spells, potions, success):
        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        potions.sort()
        for i in range(n):
            left, right = 0, m - 1
            while left <= right:
                mid = (left + right) // 2
                if spells[i] * potions[mid] >= success:
                    pairs[i] = m - mid
                    break
                elif spells[i] * potions[mid] < success:
                    left = mid + 1
                else:
                    right = mid - 1
        return pairs