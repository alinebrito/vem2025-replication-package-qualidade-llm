class Solution:
    def maxSubarraySumCircular(self, nums):
        n = len(nums)
        max_sum = nums[0]
        min_sum = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        total_sum = nums[0]

        for i in range(1, n):
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(max_sum, curr_max)

            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(min_sum, curr_min)

            total_sum += nums[i]

        if total_sum == min_sum:
            return max_sum
        else:
            return max(max_sum, total_sum - min_sum)