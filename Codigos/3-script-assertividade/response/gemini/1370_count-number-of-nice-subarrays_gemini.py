class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count = 0
        prefix = [0] * (len(nums) + 1)
        odd = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                odd += 1
            prefix[odd] += 1
        for left in range(len(nums)):
            right = left + k
            if right <= len(prefix) - 1:
                count += prefix[right]
        return count