class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n - 1):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return res