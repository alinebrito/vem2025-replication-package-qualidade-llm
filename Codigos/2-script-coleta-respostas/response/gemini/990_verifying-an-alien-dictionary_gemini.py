class Solution:
    def isAlienSorted(self, W: List[str], O: str) -> bool:
        alpha = {O[i]: i for i in range(len(O))}
        for i in range(len(W) - 1):
            w1, w2 = W[i], W[i + 1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if alpha[w1[j]] > alpha[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True