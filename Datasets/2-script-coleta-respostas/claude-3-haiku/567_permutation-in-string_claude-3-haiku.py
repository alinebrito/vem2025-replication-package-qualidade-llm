class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w = Counter(s1), len(s1)
        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
                if not any(v > 0 for v in cntr.values()):
                    return True
            if i >= w and s2[i-w] in cntr:
                cntr[s2[i-w]] += 1
        return False