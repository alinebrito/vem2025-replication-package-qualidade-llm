class Solution:
    def findUnsortedSubarray(self, N: List[int]) -> int:
        lenN, left, right = len(N) - 1, -1, -1
        for i in range(lenN):
            if N[i] > N[i + 1]:
                left = i
                break
        if left == -1:
            return 0
        for i in range(lenN, 0, -1):
            if N[i] < N[i - 1]:
                right = i
                break
        minV, maxV = min(N[left : right + 1]), max(N[left : right + 1])
        for i in range(0, left):
            if N[i] > minV:
                left = i
                break
        for i in range(lenN, right, -1):
            if N[i] < maxV:
                right = i
                break
        return right - left + 1