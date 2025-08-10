class Solution:
    def permute(self, nums):
        res = []
        self.backtrack(nums, [], res)
        return res

    def backtrack(self, nums, path, res):
        if not nums:
            res.append(path[:])
            return
        for i in range(len(nums)):
            path.append(nums[i])
            self.backtrack(nums[:i] + nums[i+1:], path, res)
            path.pop()