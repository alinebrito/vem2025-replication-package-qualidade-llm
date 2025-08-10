class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False
        num_dict = {}
        for i in range(len(nums)):
            for j in range(max(0, i - indexDiff), i):
                if abs(nums[i] - nums[j]) <= valueDiff:
                    return True
            num_dict[nums[i]] = i
        return False