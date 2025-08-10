class Solution:
    def isIsomorphic(self, s, t):
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] not in s2t:
                s2t[s[i]] = t[i]
            if t[i] not in t2s:
                t2s[t[i]] = s[i]
            if s2t[s[i]] != t[i] or t2s[t[i]] != s[i]:
                return False
        return True