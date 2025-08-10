class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [list(i) for i in reversed(list(zip(*matrix)))]