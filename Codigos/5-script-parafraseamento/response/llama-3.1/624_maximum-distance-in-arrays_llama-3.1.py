class Solution:
    def maxDistance(self, arrays):
        return max(max(arrays[i]) - min(arrays[i-1]) for i in range(1, len(arrays)))