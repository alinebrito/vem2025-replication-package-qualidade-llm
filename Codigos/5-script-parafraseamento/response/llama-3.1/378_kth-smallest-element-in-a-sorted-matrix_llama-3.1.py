class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        n = len(matrix)
        for i in range(n):
            temp.append((matrix[i][0], i, 0))
        temp.sort()
        for _ in range(k):
            val, row, col = temp.pop(0)
            if col < n - 1:
                temp.append((matrix[row][col + 1], row, col + 1))
                temp.sort()
        return val