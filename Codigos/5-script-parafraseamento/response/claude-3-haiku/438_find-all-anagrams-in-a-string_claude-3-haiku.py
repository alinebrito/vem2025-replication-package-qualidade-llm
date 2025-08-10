class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = {}, [], len(p), len(s)
        for c in p:
            hm[c] = hm.get(c, 0) + 1
        left = 0
        for right in range(sL):
            hm[s[right]] = hm.get(s[right], 0) - 1
            if hm[s[right]] == 0:
                del hm[s[right]]
            if len(hm) == 0:
                res.append(left)
            if right - left + 1 == pL:
                hm[s[left]] = hm.get(s[left], 0) + 1
                if hm[s[left]] > 0:
                    del hm[s[left]]
                left += 1