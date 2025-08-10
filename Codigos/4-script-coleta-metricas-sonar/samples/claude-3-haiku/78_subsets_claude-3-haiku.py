class Solution:
    def subsets(self, nums):
        ret = []
        self.backtrack(nums, 0, [], ret)
        return ret

    def backtrack(self, nums, start, subset, ret):
        ret.append(subset[:])
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.backtrack(nums, i + 1, subset, ret)
            subset.pop()