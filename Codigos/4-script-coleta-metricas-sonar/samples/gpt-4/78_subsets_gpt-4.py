class Solution:
    def subsets(self, nums):
        ret = []
        def backtrack(start, path):
            ret.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        backtrack(0, [])
        return ret  