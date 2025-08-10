class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))] + [list(x) for x in zip(*A[::-1])]
        return A