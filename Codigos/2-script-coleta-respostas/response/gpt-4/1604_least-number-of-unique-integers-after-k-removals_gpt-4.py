class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hp = list(collections.Counter(arr).values())
        hp.sort()
        unique_count = len(hp)
        for count in hp:
            if k >= count:
                k -= count
                unique_count -= 1
            else:
                break
        return unique_count