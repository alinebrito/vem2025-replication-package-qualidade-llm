class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)
        left = 0
        right = nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            count = 0
            j = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left