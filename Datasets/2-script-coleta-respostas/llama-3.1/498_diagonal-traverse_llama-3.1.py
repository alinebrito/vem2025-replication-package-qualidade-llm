class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diagonal = {}
        for i in range(m):
            for j in range(n):
                if i + j not in diagonal:
                    diagonal[i + j] = []
                diagonal[i + j].append(mat[i][j])
        res = []
        for k in range(m + n - 1):
            if k % 2 == 0:
                res += diagonal[k][::-1]
 else:
                res += diagonal[k]
        return res