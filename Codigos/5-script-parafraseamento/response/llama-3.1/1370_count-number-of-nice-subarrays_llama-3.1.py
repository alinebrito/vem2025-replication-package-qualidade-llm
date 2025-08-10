class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count = 0
        odd_count = 0
        left = 0
        odd_indices = [-1]
        
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_count += 1
                odd_indices.append(i)
            
            if odd_count > k:
                left += 1
                odd_count -= 1
            
            if odd_count == k:
                count += odd_indices[left + 1] - odd_indices[left] + 1
        
        return count