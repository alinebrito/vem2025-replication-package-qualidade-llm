class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count = 0
        odd_count = 0
        freq = [0] * (len(nums) + 1)
        freq[0] = 1
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            if odd_count >= k:
                count += freq[odd_count - k]
            freq[odd_count] += 1
        return count