class Solution:
    def smallestDistancePair(self, nums, k):
        n = len(nums)
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if self.countLessEqual(nums, mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

    def countLessEqual(self, nums, target):
        i, count = 0, 0
        for j in range(len(nums)):
            while nums[j] - nums[i] > target:
                i += 1
            count += j - i
        return count