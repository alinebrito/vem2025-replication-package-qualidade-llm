class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        C = {}
        for i, n in enumerate(nums):
            if n not in C: C[n] = [1, i, i]
            else:
                C[n][0] += 1
                C[n][2] = i
        degree = max(C.values())[0]
        ans = len(nums)
        for n in C:
            if C[n][0] == degree:
                ans = min(ans, C[n][2] - C[n][1] + 1)
        return ans