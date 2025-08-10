class Solution:
    def nextPermutation(self, nums):
        i = j = len(nums)-1
        
        # Find the first number from the right that is smaller than its next number
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # If the array is already in descending order, reverse it and return
        if i == 0:
            nums.reverse()
            return
        
        # Find the first number from the right that is greater than nums[i-1]
        while nums[j] <= nums[i-1]:
            j -= 1
        
        # Swap nums[i-1] and nums[j]
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # Reverse the subarray from i to the end
        nums[i:] = nums[i:][::-1]