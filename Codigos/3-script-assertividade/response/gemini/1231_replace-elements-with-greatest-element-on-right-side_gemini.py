class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        mx = -1
        for i in range(n - 1, -1, -1):
            arr[i], mx = mx, max(mx, arr[i])
        return arr