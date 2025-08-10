class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = {}

        def backtrack(index, total):
            if index == len(nums):
                return 1 if total == S else 0
            if (index, total) in dp:
                return dp[(index, total)]

            dp[(index, total)] = backtrack(index + 1, total + nums[index]) + backtrack(index + 1, total - nums[index])
            return dp[(index, total)]

        return backtrack(0, 0)