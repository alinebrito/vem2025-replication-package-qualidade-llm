class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        ans = []
        rest = []
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        for num in arr2:
            ans.extend([num] * count[num])
            count[num] = 0
        for num in sorted(count):
            rest.extend([num] * count[num])
        return ans + rest
