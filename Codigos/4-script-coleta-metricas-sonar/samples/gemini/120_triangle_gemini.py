class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            if row == len(triangle):
                return 0
            return triangle[row][col] + min(dp(row + 1, col), dp(row + 1, col + 1))
        return dp(0, 0)