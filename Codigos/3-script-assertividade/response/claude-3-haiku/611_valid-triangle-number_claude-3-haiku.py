class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    count += k-j
                    k -= 1
                else:
                    j += 1
        return count