class Solution:
    def isIsomorphic(self, s, t):
        s2t, t2s = {}, {}
        for cs, ct in zip(s, t):
            if cs in s2t and s2t[cs] != ct:
                return False
            if ct in t2s and t2s[ct] != cs:
                return False
            s2t[cs] = ct
            t2s[ct] = cs