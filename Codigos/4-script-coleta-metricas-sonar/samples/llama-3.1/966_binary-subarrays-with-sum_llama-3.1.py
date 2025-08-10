class Solution:
    def numSubarraysWithSum(self, nums, goal):
        count = {0: 1}
        prefix_sum = 0
        res = 0
        for num in nums:
            prefix_sum += num
            res += count.get(prefix_sum - goal, 0)
            count[prefix_sum] = count.get(prefix_sum, 0) + 1
        return res