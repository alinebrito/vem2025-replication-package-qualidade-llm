class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            guess = (left + right) // 2
            count = sum(i // guess for i in range(1, n))
            if count >= k:
                right = guess - 1
            else:
                left = guess + 1
        return left