class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issubseq(s, t):
            it = iter(s)
            return all(c in it for c in t)

        return sum(issubseq(s, word) for word in words)