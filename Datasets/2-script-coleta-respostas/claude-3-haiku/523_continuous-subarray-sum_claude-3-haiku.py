class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_cache = {0:-1}
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if k != 0:
                current_sum %= k
            if current_sum in remainder_cache and i - remainder_cache[current_sum] > 1:
                return True
            if current_sum not in remainder_cache:
                remainder_cache[current_sum] = i
        return False