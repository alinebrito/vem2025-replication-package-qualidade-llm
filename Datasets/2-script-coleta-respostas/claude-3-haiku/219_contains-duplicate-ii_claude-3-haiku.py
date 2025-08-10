class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic and abs(i - dic[num]) <= k:
                return True
            dic[num] = i
        return False