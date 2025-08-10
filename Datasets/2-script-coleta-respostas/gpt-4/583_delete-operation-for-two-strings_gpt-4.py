class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(w1, w2, i, j):
            if i == len(w1):
                return len(w2) - j
            if j == len(w2):
                return len(w1) - i
            if w1[i] == w2[j]:
                return solve(w1, w2, i + 1, j + 1)
            return 1 + min(solve(w1, w2, i + 1, j), solve(w1, w2, i, j + 1))
        
        return solve(word1, word2, 0, 0)