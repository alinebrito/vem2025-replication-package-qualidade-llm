class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 2
        if len(nums) < k:
            return len(nums)
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k