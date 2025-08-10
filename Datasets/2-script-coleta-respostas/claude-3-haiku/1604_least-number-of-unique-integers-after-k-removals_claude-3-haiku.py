class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hp = list(collections.Counter(arr).values())
        hp.sort()
        res = 0
        for i in range(len(hp)):
            if k >= hp[i]:
                k -= hp[i]
                res += 1
            else:
                break
        return res