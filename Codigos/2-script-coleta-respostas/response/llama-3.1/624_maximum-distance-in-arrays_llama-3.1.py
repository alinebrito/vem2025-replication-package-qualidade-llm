class Solution:
    def maxDistance(self, arrays):
        max1, min1 = float('-inf'), float('inf')
        for arr in arrays:
            max1 = max(max1, arr[-1])
            min1 = min(min1, arr[0])
        return max(max1 - min1, max1 + min1)