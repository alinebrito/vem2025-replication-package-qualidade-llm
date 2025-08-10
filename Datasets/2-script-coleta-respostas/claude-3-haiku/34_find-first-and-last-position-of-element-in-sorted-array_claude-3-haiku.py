class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, -1
        
        # Find the leftmost position of the target
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                right = mid
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        # Find the rightmost position of the target
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                left = mid
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return [left, right]