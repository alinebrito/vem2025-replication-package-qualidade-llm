class Solution:
    def subarraySum(self, nums, k):
        count = 0
        cum_sum = 0
        lookup = {0: 1}
        for num in nums:
            cum_sum += num
            if (cum_sum - k) in lookup:
                count += lookup[cum_sum - k]
            lookup[cum_sum] = lookup.get(cum_sum, 0) + 1
        return count