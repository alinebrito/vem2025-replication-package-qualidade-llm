class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        length = len(arr)
        for i in range(length - 1, -1, -1):
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < length:
                    arr[i + zeroes] = 0
                if i + zeroes + 1 < length:
                    arr[i + zeroes + 1] = 0
            elif i + zeroes < length:
                arr[i + zeroes] = arr[i]