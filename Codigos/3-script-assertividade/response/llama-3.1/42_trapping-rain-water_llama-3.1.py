class Solution:
    def sumBackets(self, height: list[int], left, right):
        water = 0
        i, j = left, right
        max_left, max_right = height[left], height[right]
        
        while i <= j:
            if max_left < max_right:
                i += 1
                if height[i] > max_left:
                    max_left = height[i]
                else:
                    water += max_left - height[i]
            else:
                j -= 1
                if height[j] > max_right:
                    max_right = height[j]
                else:
                    water += max_right - height[j]
        
        return water