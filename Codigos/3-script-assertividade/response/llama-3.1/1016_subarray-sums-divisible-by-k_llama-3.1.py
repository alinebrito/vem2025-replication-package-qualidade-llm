class Solution:
 def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [1] + [0]* (k - 1)
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            result += count[prefix_sum]
            count[prefix_sum] += 1
        return result