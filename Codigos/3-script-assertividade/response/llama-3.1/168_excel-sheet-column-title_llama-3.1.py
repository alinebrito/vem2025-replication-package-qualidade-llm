class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        res = ''
        while columnNumber > 0:
            columnNumber -= 1
            res = capitals[columnNumber % 26] + res
            columnNumber //= 26
        return res