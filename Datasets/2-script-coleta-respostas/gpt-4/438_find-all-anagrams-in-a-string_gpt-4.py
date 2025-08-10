class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        for char in p:
            hm[char] += 1
        for i in range(sL):
            if i >= pL:
                if hm[s[i - pL]] == 1:
                    del hm[s[i - pL]]
                else:
                    hm[s[i - pL]] -= 1
            hm[s[i]] += 1
            if hm == defaultdict(int, {char: p.count(char) for char in p}):
                res.append(i - pL + 1)
        return res