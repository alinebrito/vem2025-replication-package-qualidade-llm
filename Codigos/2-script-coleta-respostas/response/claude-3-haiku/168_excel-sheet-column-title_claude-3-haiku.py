class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(capitals[columnNumber % 26])
            columnNumber //= 26
        return ''.join(reversed(result))