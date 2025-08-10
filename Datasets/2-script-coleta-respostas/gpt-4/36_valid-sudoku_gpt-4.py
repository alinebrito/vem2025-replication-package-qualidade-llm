class Solution:
    def isValidSudoku(self, board):
        def is_row_valid(board):
            for row in board:
                seen = set()
                for num in row:
                    if num != '.':
                        if num in seen:
                            return False  
                        seen.add(num)
            return True
        
        def is_col_valid(board):
            for col in range(9):
                seen = set()
                for row in range(9):
                    num = board[row][col]
                    if num != '.':
                        if num in seen:
                            return False  
                        seen.add(num)
            return True
        
        def is_box_valid(board):
            for box_row in range(3):
                for box_col in range(3):
                    seen = set()
                    for row in range(box_row * 3, box_row * 3 + 3):
                        for col in range(box_col * 3, box_col * 3 + 3):
                            num = board[row][col]
                            if num != '.':
                                if num in seen:
                                    return False  
                                seen.add(num)
            return True

        return is_row_valid(board) and is_col_valid(board) and is_box_valid(board)