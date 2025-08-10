class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()
        total = 0
        prev = -1
        for num in nums:
            if num <= prev:
                total += prev - num + 1
                prev += 1
            else:
                prev = num
        return total