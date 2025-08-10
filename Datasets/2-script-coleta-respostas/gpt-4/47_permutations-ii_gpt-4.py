class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        def backtrack(path, visited):
            if len(path) == len(nums):
                res.append(path[:])
                return  
            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue  
                visited[i] = True  
                path.append(nums[i])
                backtrack(path, visited)
                path.pop()
                visited[i] = False  
        backtrack([], [False] * len(nums))
        return res  