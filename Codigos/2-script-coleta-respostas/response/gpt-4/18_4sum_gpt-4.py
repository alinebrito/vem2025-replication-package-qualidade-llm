class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        result = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                left, right = j + 1, n - 1  
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1  
                        right -= 1  
                    elif total < target:
                        left += 1  
                    else:
                        right -= 1  
        return [list(quad) for quad in result]