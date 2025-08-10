class Solution:
    def canJump(self, nums):
        m = 0
        for i, num in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + num)
        return True