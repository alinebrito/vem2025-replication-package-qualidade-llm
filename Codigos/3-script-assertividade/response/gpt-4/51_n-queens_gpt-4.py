class Solution:
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            row = len(queens)
            if row == n:
                board = []
                for q in queens:
                    board.append("." * q + "Q" + "." * (n - q - 1))
                output.append(board)
                return  
            for col in range(n):
                if col in queens or row - col in xy_dif or row + col in xy_sum:
                    continue  
                DFS(queens + [col], xy_dif + [row - col], xy_sum + [row + col])

        output = []
        DFS([], [], [])
        return output  