class Solution(object):
    def maxDistance(self, arrays):
        n = len(arrays)
        max_dist = 0
        min_val, max_val = float('inf'), float('-inf')
        
        for i in range(n):
            max_dist = max(max_dist, max(arrays[i]) - min_val, max_val - min(arrays[i]))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_dist