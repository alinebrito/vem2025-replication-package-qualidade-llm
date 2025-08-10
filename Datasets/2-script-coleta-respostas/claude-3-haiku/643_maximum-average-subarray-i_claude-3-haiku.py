class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_sum = sum(nums[:k])
        current_sum = max_sum
        for i in range(k, n):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum / k