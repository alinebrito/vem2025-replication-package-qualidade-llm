class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for x in s:
            lo += 1 if x == '(' else -1
            hi += 1 if x != ')' else -1
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0