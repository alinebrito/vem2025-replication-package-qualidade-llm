class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        seen = [False] * (n + 1)
        duplicate = 0
        for num in nums:
            if seen[num]:
                duplicate = num
            else:
                seen[num] = True
        missing = 0
        for i in range(1, n + 1):
            if not seen[i]:
                missing = i
                break
        return [duplicate, missing]