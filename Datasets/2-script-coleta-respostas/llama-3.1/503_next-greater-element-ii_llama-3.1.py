class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        
        for i in range(n * 2):
            while stack and stack[-1] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        
        return res