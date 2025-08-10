class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        val = 0
        for i in range(len(num)):
            val = val * 10 + num[i]
        return [int(x) for x in str(val + k)]