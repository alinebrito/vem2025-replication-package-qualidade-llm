class Solution:
    def findErrorNums(self, nums):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        duplicate = None
        missing = None
        for i in range(1, len(nums) + 1):
            if i not in count:
                missing = i
            elif count[i] == 2:
                duplicate = i
        return [duplicate, missing]