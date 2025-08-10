class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        res = ''
        for i in range(len(s)):
            if i > 0 and i % k == 0:
                res += '-'
            res += s[i]
        return res[::-1]