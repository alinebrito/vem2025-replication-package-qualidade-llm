class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def atMostK(k):
            count = 0  
            left = 0  
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    k -= 1  
                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1  
                    left += 1  
                count += right - left + 1  
            return count

        return atMostK(k) - atMostK(k - 1)