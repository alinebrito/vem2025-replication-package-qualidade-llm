class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numsSorted = sorted(nums)
        left = len(nums)
        right = 0
        for i in range(len(nums)):
            if numsSorted[i] != nums[i]:
                left = min(left, i)
                right = max(right, i)
        return right - left + 1 if right > left else 0