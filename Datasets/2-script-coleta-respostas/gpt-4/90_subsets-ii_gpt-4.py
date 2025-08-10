class Solution:
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        def backtrack(start, path):
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue  
                res.append(path + [nums[i]])
                backtrack(i + 1, path + [nums[i]])
        backtrack(0, [])
        return res  