class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if t < 0: return False
        for i in range(len(nums)):
            for j in range(i + 1, min(i + indexDiff + 1, len(nums))):
                if abs(nums[i] - nums[j]) <= valueDiff:
                    return True
        return False