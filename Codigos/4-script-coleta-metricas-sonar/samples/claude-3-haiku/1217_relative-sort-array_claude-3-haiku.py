class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans, cnt = [], collections.Counter(arr1)
        for num in arr2:
            ans.extend([num] * cnt[num])
            cnt[num] = 0
        return ans + sorted(num for num in cnt if cnt[num] > 0)