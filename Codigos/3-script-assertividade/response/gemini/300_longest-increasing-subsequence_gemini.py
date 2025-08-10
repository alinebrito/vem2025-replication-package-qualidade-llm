class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            i = 0
            j = size
            while i < j:
                mid = (i + j) // 2
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = num
            if i == size:
                size += 1
        return size