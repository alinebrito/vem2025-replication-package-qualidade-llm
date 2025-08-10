class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        n = len(num)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = num[i] + num[left] + num[right]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target
        
        return closest_sum