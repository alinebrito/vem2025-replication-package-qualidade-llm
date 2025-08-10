class Solution(object):
    def numberOfSubarrays(self, nums, k):
        odd_count = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_count += 1
            if odd_count == k:
                result += 1
            if odd_count > k:
                odd_count -= 1
                for j in range(i, len(nums)):
                    if nums[j] % 2 == 1:
                        odd_count -= 1
                    result += 1
                    if odd_count == 0:
                        break
        return result