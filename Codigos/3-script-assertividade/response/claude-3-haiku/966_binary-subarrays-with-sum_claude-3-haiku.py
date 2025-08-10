class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = 0
        curr_sum = 0
        prefix_sum = {0: 1}
        for num in nums:
            curr_sum += num
            if curr_sum - goal in prefix_sum:
                count += prefix_sum[curr_sum - goal]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        return count