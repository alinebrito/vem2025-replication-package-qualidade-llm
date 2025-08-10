class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0: return False
        buckets = {}
        for i, num in enumerate(nums):
            bucket_id = num // (valueDiff + 1)
            if bucket_id in buckets or (bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff) or (bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff):
                return True
            buckets[bucket_id] = num
            if len(buckets) > indexDiff:
                del buckets[nums[i - indexDiff] // (valueDiff + 1)]
        return False