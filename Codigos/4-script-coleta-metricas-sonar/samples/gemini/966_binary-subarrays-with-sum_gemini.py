class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = 0
        prefix_sum_counts = {0: 1}
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            complement = prefix_sum - goal
            if complement in prefix_sum_counts:
                count += prefix_sum_counts[complement]
            prefix_sum_counts[prefix_sum] = prefix_sum_counts.get(prefix_sum, 0) + 1
        return count