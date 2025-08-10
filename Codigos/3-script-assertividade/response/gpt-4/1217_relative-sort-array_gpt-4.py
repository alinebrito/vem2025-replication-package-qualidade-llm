class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans, cnt = [], {}
        for num in arr1:
            cnt[num] = cnt.get(num, 0) + 1
        for num in arr2:
            ans.extend([num] * cnt[num])
            del cnt[num]
        for num in sorted(cnt.keys()):
            ans.extend([num] * cnt[num])
        return ans