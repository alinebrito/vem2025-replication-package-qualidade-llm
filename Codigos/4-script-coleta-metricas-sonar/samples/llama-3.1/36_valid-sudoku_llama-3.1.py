class Solution:
    def isValidSudoku(self, board):
        def is_valid(nums):
            nums = [num for num in nums if num != '.']
            return len(set(nums)) == len(nums)

        for i in range(9):
            if not is_valid(board[i]):
                return False
            if not is_valid([board[j][i] for j in range(9)]):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not is_valid(nums):
                    return False

        return True