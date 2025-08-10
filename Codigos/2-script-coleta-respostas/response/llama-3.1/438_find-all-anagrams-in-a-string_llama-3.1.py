class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        hm, res, pL, sL = {}, [], len(p), len(s)
        for c in p:
            hm[c] = hm.get(c, 0) + 1
        for i in range(sL - pL + 1):
            temp = {}
            for j in range(pL):
                temp[s[i + j]] = temp.get(s[i + j], 0) + 1
            if temp == hm:
                res.append(i)
        return res