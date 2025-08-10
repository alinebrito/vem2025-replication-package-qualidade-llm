class Solution:
    def findAnagrams(self, s: str, p: str):
        hm, res, pL, sL = {}, [], len(p), len(s)
        if sL < pL: return res  
        for char in p: hm[char] = hm.get(char, 0) + 1  
        for i in range(sL):
            if s[i] in hm: hm[s[i]] -= 1  
            if i >= pL: 
                if s[i - pL] in hm: hm[s[i - pL]] += 1  
            if all(v == 0 for v in hm.values()): res.append(i - pL + 1)
        return res  