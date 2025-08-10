class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 3:
            return True
        else:
            return not (n % 4 == 0)