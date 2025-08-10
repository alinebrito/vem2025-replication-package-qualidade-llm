class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.backtrack(nums, [], res, [False] * len(nums))
        return res

    def backtrack(self, nums, temp, res, used):
        if len(temp) == len(nums):
            res.append(temp[:])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            used[i] = True
            temp.append(nums[i])
            self.backtrack(nums, temp, res, used)
            used[i] = False
            temp.pop()