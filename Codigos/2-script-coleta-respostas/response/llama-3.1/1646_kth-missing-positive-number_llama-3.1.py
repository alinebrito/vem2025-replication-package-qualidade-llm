class Solution(object):
    def findKthPositive(self, arr, k):
        i, num = 0, 1
        while k > 0:
            if i < len(arr) and arr[i] == num:
                i += 1
            else:
                k -= 1
            num += 1
        return num - 1