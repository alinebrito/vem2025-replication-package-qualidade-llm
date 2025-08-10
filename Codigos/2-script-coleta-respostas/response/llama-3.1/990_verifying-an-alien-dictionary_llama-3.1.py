class Solution:
    def isAlienSorted(self, W: List[str], O: str) -> bool:
        alpha = {O[i]: i for i in range(len(O))}
        for i in range(len(W) - 1):
            for j in range(min(len(W[i]), len(W[i + 1]))):
                if alpha[W[i][j]] < alpha[W[i + 1][j]]:
                    break
                elif alpha[W[i][j]] > alpha[W[i + 1][j]]:
                    return False
            else:
                if len(W[i]) > len(W[i + 1]):
                    return False
        return True