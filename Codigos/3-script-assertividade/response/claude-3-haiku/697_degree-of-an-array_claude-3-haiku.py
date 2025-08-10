class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        C = {}
        for i, x in enumerate(nums):
            if x not in C:
                C[x] = [i, i, 1]
            else:
                C[x][1] = i
                C[x][2] += 1
        return min(x[1] - x[0] + 1 for x in C.values() if x[2] == max(C.values(), key=lambda x: x[2])[2])