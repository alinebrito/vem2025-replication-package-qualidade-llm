class Solution:
    def rotate(self, A):
        A[:] = list(zip(*A[::-1]))