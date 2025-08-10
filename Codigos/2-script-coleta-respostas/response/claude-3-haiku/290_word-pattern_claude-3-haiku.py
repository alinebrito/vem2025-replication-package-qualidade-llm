class Solution:
    def wordPattern(self, pattern, s):
        s = s.split()
        if len(pattern) != len(s):
            return False
        p2w, w2p = {}, {}
        for i in range(len(pattern)):
            if pattern[i] in p2w:
                if p2w[pattern[i]] != s[i]:
                    return False
            else:
                p2w[pattern[i]] = s[i]
            if s[i] in w2p:
                if w2p[s[i]] != pattern[i]:
                    return False
            else:
                w2p[s[i]] = pattern[i]
        return True