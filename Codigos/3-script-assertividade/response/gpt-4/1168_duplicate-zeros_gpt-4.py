class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if arr[i] == 0:
                zeroes -= 1  
                if i + zeroes < n:
                    arr[i + zeroes] = 0  
                if i + zeroes + 1 < n:
                    arr[i + zeroes + 1] = 0 if i + zeroes + 1 < n else arr[i + zeroes + 1]
            elif i + zeroes < n:
                arr[i + zeroes] = arr[i]