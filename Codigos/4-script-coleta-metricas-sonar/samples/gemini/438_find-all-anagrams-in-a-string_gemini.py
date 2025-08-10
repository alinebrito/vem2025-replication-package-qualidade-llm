class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        hm, res, pL, sL = {}, [], len(p), len(s)
        if pL > sL: return []

        # build hashmap out of p
        for ch in p: hm[ch] = hm.get(ch, 0) + 1

        # initial window
        for i in range(pL): 
            if s[i] in hm: hm[s[i]] -= 1

        # slide window from left to right
        for i in range(sL - pL + 1):
            # check if current window is an anagram
            if all(v == 0 for v in hm.values()): 
                res.append(i)

            # slide window to right: 
            # 1. remove leftmost char count from hashmap
            if i < sL - pL:
                if s[i] in hm:
                    hm[s[i]] += 1
            # 2. add rightmost char count to hashmap
                if s[i + pL] in hm: 
                    hm[s[i + pL]] -= 1
        return res