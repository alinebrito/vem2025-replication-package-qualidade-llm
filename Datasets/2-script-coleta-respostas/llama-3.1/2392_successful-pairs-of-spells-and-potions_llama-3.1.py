class Solution:
    def successfulPairs(self, spells, potions, success):
        n = len(spells)
        m = len(potions)
        potions.sort()
        result = []
        for spell in spells:
            target = (success + spell - 1) // spell
            count = 0
            left = 0
            right = m -1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= target:
                    ans = mid
                    right = mid -1
                else:
                    left = mid + 1
            if ans != -1:
                count = m - ans
            result.append(count)
        return result