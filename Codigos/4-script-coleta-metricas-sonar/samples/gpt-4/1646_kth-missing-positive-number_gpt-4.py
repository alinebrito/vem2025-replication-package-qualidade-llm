class Solution(object):
    def findKthPositive(self, arr, k):
        missing_count = 0
        current = 1
        index = 0
        while missing_count < k:
            if index < len(arr) and arr[index] == current:
                index += 1
            else:
                missing_count += 1
                if missing_count == k:
                    return current
            current += 1