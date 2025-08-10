class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = []
        for row in mat:
            for num in row:
                flatten.append(num)
        if len(flatten) != r * c:
            return mat
        else:
            new_mat = []
            for i in range(0, len(flatten), c):
                new_mat.append(flatten[i:i+c])
            return new_mat