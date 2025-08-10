class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count = 0
        odd_count = 0
        left = 0
        odd_map = {0: 1}
        
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
            
            if odd_count - k in odd_map:
                count += odd_map[odd_count - k]
            
            if odd_count in odd_map:
                odd_map[odd_count] += 1
            else:
                odd_map[odd_count] = 1
        
        return count