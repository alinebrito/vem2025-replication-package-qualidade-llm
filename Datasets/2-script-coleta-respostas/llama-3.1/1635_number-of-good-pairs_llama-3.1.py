class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return sum((count[num] * (count[num] - 1)) // 2 for num in count)