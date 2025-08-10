class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        for c in p:
            hm[c] += 1
        left = 0
        for right in range(sL):
            hm[s[right]] -= 1
            if hm[s[right]] == 0:
                del hm[s[right]]
            if len(hm) == 0:
                res.append(left)
            if right - left + 1 == pL:
                hm[s[left]] += 1
                if hm[s[left]] > 0:
                    del hm[s[left]]
                left += 1
        return res