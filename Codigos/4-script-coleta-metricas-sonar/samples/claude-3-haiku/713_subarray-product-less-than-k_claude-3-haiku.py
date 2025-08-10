class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        n = len(nums)
        left, right = 0, 0
        product = 1
        count = 0
        
        while right < n:
            product *= nums[right]
            
            while product >= k:
                product //= nums[left]
                left += 1
            
            count += right - left + 1
            right += 1
        
        return count