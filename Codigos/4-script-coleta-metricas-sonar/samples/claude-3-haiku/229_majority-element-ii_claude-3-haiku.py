class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        n = len(nums)
        threshold = n // 3
        return [num for num, c in count.items() if c > threshold]