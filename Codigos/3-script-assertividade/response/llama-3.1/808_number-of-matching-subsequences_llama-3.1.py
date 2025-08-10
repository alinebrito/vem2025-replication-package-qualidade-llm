class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issubseq(s, t):
            t_idx = 0
            for char in s:
                if t_idx < len(t) and char == t[t_idx]:
                    t_idx += 1
            return t_idx == len(t)

        return sum(1 for word in words if issubseq(s, word))