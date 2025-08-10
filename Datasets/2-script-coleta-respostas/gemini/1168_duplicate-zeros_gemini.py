class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        i = n - 1
        j = n + zeroes - 1

        while i != j:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = arr[i]
            i -= 1
            j -= 1