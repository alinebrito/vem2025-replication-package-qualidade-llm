class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        C = {}
        for i in range(len(nums)):
            if nums[i] not in C:
                C[nums[i]] = [i,i]
            else:
                C[nums[i]][1] = i
        max_freq = max([nums.count(x) for x in set(nums)])
        min_len = len(nums)
        for k,v in C.items():
            if nums.count(k) == max_freq:
                min_len = min(min_len,v[1]-v[0]+1)
        return min_len