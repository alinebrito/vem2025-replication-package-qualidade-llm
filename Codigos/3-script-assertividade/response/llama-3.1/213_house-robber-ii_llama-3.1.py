class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        def simple_rob(houses):
            prev, curr = 0, 0
            for money in houses:
                prev, curr = curr, max(prev + money, curr)
            return curr
        
        return max(simple_rob(nums[:-1]), simple_rob(nums[1:]))