class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        if not mat or not mat[0]:
            return False  
        m, n = len(mat), len(mat[0])
        row, col = 0, n - 1  
        while row < m and col >= 0:
            if mat[row][col] == target:
                return True  
            elif mat[row][col] > target:
                col -= 1  
            else:
                row += 1  
        return False  