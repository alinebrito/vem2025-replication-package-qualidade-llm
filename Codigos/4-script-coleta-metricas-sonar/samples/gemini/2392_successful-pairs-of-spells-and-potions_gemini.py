class Solution:
    def successfulPairs(self, spells, potions, success):
        n = len(spells)
        m = len(potions)
        potions.sort()
        pairs = [0] * n
        for i in range(n):
            left = 0
            right = m - 1
            while left <= right:
                mid = (left + right) // 2
                if spells[i] * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            pairs[i] = m - left
        return pairs