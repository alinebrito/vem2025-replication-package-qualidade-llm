class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w = {}, len(s1)
        for c in s1:
            cntr[c] = cntr.get(c, 0) + 1
        l = 0
        for r in range(len(s2)):
            cntr[s2[r]] = cntr.get(s2[r], 0) - 1
            if r >= w - 1:
                if all(x == 0 for x in cntr.values()):
                    return True
                cntr[s2[l]] = cntr.get(s2[l], 0) + 1
                l += 1