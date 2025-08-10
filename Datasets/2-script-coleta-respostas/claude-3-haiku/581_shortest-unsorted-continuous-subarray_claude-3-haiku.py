class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lenN, left, right = len(nums) - 1, -1, -1
        
        for i in range(lenN):
            if nums[i] > nums[i+1]:
                if left == -1:
                    left = i
                right = i+1
        
        if left == -1:
            return 0
        
        min_val = min(nums[left:right+1])
        max_val = max(nums[left:right+1])
        
        while left > 0 and nums[left-1] > min_val:
            left -= 1
        
        while right < lenN and nums[right] < max_val:
            right += 1
        
        return right - left + 1