class Solution:
    def __init__(self, matrix):
        self.dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):