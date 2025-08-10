class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        num_set = set()
        duplicate = -1  
        for num in nums:
            if num in num_set:
                duplicate = num  
            else:
                num_set.add(num)
        missing = sum(range(1, n + 1)) - sum(num_set)
        return [duplicate, missing]