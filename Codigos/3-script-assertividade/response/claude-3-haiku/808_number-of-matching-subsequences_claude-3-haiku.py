class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issubseq(s, t):
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    j += 1
                i += 1
            return j == len(t)

        count = 0
        for word in words:
            if issubseq(s, word):
                count += 1
        return count