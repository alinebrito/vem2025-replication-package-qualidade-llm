class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w = Counter(s1), len(s1)
        for i in range(len(s2) - w + 1):
            if Counter(s2[i: i + w]) == cntr:
                return True
        return False