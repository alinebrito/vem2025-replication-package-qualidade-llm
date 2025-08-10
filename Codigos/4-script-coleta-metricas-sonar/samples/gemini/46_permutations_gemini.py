class Solution:
    def permute(self, nums):
        res = []
        def backtrack(index):
            if index == len(nums):
                res.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index + 1)
                nums[index], nums[i] = nums[i], nums[index]
        backtrack(0)
        return res