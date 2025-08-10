class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_cache = {0: -1}
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            if k != 0:
                total_sum %= k
            if total_sum in remainder_cache:
                if i - remainder_cache[total_sum] > 1:
                    return True
            else:
                remainder_cache[total_sum] = i
        return False