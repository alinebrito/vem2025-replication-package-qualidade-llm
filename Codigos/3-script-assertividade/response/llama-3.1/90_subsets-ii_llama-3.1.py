class Solution:
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(len(res), len(nums) - i):
                res.append(res[j] + [nums[i]])
        return res