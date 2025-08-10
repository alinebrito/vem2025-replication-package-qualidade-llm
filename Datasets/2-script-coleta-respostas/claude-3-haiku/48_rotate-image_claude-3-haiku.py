class Solution:
    def rotate(self, matrix):
        matrix[:] = list(map(list, zip(*matrix[::-1])))