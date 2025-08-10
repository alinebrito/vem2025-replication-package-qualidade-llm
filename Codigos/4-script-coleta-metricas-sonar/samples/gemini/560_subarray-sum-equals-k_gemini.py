class Solution:
    def subarraySum(self, nums, k):
        prefixSum = {0: 1}
        currSum = 0
        count = 0
        for num in nums:
            currSum += num
            if currSum - k in prefixSum:
                count += prefixSum[currSum - k]
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        return count