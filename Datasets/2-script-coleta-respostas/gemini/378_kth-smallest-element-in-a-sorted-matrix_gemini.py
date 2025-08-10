class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        for i in matrix:
            temp += i
        temp.sort()