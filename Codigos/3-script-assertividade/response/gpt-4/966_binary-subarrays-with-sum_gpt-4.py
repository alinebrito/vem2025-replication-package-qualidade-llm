class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = {0: 1}
        total = 0
        result = 0
        for num in nums:
            total += num
            if total - goal in count:
                result += count[total - goal]
            count[total] = count.get(total, 0) + 1
        return result