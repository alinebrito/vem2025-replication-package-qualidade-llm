class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans, cnt = [], collections.Counter(arr1)
        for i in arr2:
            ans.extend([i] * cnt.pop(i))
        return ans + sorted(cnt.elements())