class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        C = {}
        for i, num in enumerate(nums):
            if num not in C:
                C[num] = [i, i]
            else:
                C[num][1] = i
        degree = max(len(list(group)) for key, group in groupby(nums))
        return min(C[num][1] - C[num][0] + 1 for num in C if len(list(groupby(nums))[0]) == degree)