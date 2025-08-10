class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def backtrack(index, total):
            if index == len(nums):
                return 1 if total == S else 0  
            return backtrack(index + 1, total + nums[index]) + backtrack(index + 1, total - nums[index])
        
        return backtrack(0, 0)