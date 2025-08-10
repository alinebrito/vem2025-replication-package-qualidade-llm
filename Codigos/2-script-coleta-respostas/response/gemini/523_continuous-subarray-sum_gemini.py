class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_cache = {0:-1}
        current_sum = 0
        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % k
            if current_sum in remainder_cache:
                if i - remainder_cache[current_sum] >= 2:
                    return True
            else:
                remainder_cache[current_sum] = i
        return False