class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        
        def backtrack(index, current):
            if index == len(nums):
                res.append(current.copy())
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                if not visited[i]:
                    visited[i] = True
                    current.append(nums[i])
                    backtrack(index + 1, current)
                    current.pop()
                    visited[i] = False
        
        visited = [False] * len(nums)
        backtrack(0, [])
        return res