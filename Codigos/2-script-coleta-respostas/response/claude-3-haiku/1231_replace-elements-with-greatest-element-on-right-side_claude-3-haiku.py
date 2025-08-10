class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        max_right = -1
        for i in range(n-1, -1, -1):
            curr = arr[i]
            arr[i] = max_right
            max_right = max(max_right, curr)
        return arr