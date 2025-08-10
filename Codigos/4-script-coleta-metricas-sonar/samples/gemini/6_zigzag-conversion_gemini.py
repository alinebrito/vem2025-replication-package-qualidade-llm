class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        row = 0
        direction = 1
        for char in s:
            rows[row] += char
            row += direction
            if row == numRows - 1 or row == 0:
                direction *= -1
        return "".join(rows)