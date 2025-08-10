class Solution:
    def findUnsortedSubarray(self, N: List[int]) -> int:
        lenN, left, right = len(N) - 1, -1, -1
        for i in range(lenN):
            if N[i] >= N[0]:
                right = i
        for i in range(lenN, -1, -1):
            if N[i] <= N[-1]:
                left = i