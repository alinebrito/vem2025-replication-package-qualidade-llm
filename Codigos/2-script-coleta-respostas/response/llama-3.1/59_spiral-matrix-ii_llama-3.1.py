class Solution:
    def generateMatrix(self, n):
        A, lo = [[0] * n for _ in range(n)], n * n + 1
        i, j, di, dj = 0, 0, 0, 1
        while lo > 1:
            A[i][j] = lo - 1
            lo -= 1
            if A[(i + di) % n][(j + dj) % n] == 0:
                i += di
                j += dj
            else:
                di, dj = dj, -di
        return A